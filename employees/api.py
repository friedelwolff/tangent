from django.conf import settings
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

    def _api_helper(self, endpoint):
        #TODO: cache based on token and endpoint
        headers = {"Authorization": "Token %s" % self.token}
        try:
            r = requests.get(settings.API_URL + endpoint, headers=headers)
            r.raise_for_status()
            return r.json()
        except (requests.exceptions.RequestException, ValueError) as e:
            raise WebClientError() from e

    def get_employees(self, request):
        return self._api_helper('employee/')


if settings.MOCK_API:
    from employees.tests.mock_api import WebAPIClient
