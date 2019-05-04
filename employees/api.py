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


if settings.MOCK_API:
    from employees.tests.mock_api import WebAPIClient
