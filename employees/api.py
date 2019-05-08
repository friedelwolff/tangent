from urllib.parse import urlencode

from django.conf import settings
from django.core.cache import cache
import requests


class WebClientError(Exception):
    pass


class WebAPIClient:
    def __init__(self, token):
        self.token = token

    @classmethod
    def from_auth(cls, username, password):
        params = {"username": username, "password": password}
        try:
            r = requests.post(settings.API_AUTH_URL, json=params)
            r.raise_for_status()
            return cls(r.json()["token"])
        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            raise WebClientError() from e

    @classmethod
    def from_request(cls, request):
        return cls(request.session['api_token'])

    def _api_helper(self, endpoint, params=None):
        encoded_params = urlencode(params or {})
        cache_key = "API:{}:{}?{}".format(self.token, endpoint, encoded_params)
        json = cache.get(cache_key)
        if json:
            return json

        headers = {"Authorization": "Token %s" % self.token}
        try:
            r = requests.get(settings.API_URL + endpoint, headers=headers, params=params)
            r.raise_for_status()
            json = r.json()
            cache.set(cache_key, json)
            return json
        except (requests.exceptions.RequestException, ValueError) as e:
            raise WebClientError() from e

    def get_employees(self):
        return self._api_helper('employee/')

    def employees_search(self, params):
        less_params = {}
        for key, value in sorted(params.items()):
            if value:
                less_params[key] = value
        params = less_params

        if not params:
            return self.get_employees()

        return self._api_helper('employee/', params=params)

    def get_my_profile(self):
        return self._api_helper('employee/me/')

    def github_avatar_url(self, username):
        """Use the github API to get the the avatar URL."""
        if not username:
            return None
        cache_key = 'gh_avatar:{}'.format(username)
        url = cache.get(cache_key)
        if url is not None:
            # We might have cached the empty string, so we need to test for
            # None specifically.
            return url

        try:
            headers = {'Accept', 'application/vnd.github.v3+json'}
            r = requests.get('https://api.github.com/users/{}'.format(username))
            r.raise_for_status()
            url = r.json()["avatar_url"]
            cache.set(cache_key, url)
            return url
        except (requests.exceptions.RequestException, ValueError, KeyError) as e:
            # this is just not that important, so let's cache failure to avoid
            # exceeding the rate limit
            cache.set(cache_key, '')
            return None


def get_client_class():
    # simple factory method to ease testing with the mocked client
    if settings.MOCK_API:
        from employees.tests.mock_api import MockedWebAPIClient
        return MockedWebAPIClient
    return WebAPIClient
