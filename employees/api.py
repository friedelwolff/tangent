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
        if not params:
            # don't cache requests with parameters for now
            cache_key = "{}:{}".format(self.token, endpoint)
            json = cache.get(cache_key)
            if json:
                return json

        headers = {"Authorization": "Token %s" % self.token}
        try:
            r = requests.get(settings.API_URL + endpoint, headers=headers, params=params)
            r.raise_for_status()
            json = r.json()
            if not params:
                cache.set(cache_key, json)
            return json
        except (requests.exceptions.RequestException, ValueError) as e:
            raise WebClientError() from e

    def get_employees(self):
        return self._api_helper('employee/')

    def employees_search(self, params=None):
        #TODO: pop parameters with empty values
        if not params:
            return self.get_employees()

        return self._api_helper('employee/', params=params)

    def get_my_profile(self):
        return self._api_helper('employee/me/')


def get_client_class():
    # simple factory method to ease testing with the mocked client
    if settings.MOCK_API:
        from employees.tests.mock_api import MockedWebAPIClient
        return MockedWebAPIClient
    return WebAPIClient
