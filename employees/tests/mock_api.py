import json

from employees.api import WebClientError

class MockedWebAPIClient:
    def __init__(self, token):
        self.token = token

    @classmethod
    def from_auth(cls, username, password):
        if username in {'x'}:
            raise WebClientError()
        return MockedWebAPIClient('abc')

    @classmethod
    def from_request(cls, request):
        return MockedWebAPIClient('abc')

    def get_user_me(self):
        return {
               "id": 12,
               "username": "pravin.gordhan",
               "email": "pravin@axedmps.com",
               "first_name": "Pravin",
               "last_name": "Gordhan",
               "is_active": True,
               "is_staff": True,
               "is_superuser": False,
        }

    def get_employees(self):
        return json.loads('''
[
        {
            "user": {
                "id": 8,
                "username": "captain",
                "email": "captain@gmail.com",
                "first_name": "Captain",
                "last_name": "America",
                "is_active": true,
                "is_staff": true
            },
            "position": {
                "id": 1,
                "name": "Front-end Developer",
                "level": "Senior",
                "sort": 0
            },
            "phone_number": "0824478876",
            "email": "captain@gmail.com",
            "github_user": "Captain",
            "birth_date": "1981-07-30",
            "gender": "M",
            "race": "B",
            "years_worked": 3,
            "age": 37,
            "days_to_birthday": 299
        },
        {
            "user": {
                "id": 53,
                "username": "dummy1",
                "email": "dum@one.co.za",
                "first_name": "Dummy",
                "last_name": "One",
                "is_active": true,
                "is_staff": true
            },
            "position": null,
            "phone_number": null,
            "email": "dum@one.co.za",
            "github_user": null,
            "birth_date": "2018-10-04",
            "gender": null,
            "race": null,
            "years_worked": 0,
            "age": 0,
            "days_to_birthday": 0
        },
        {
            "user": {
                "id": 11,
                "username": "employee4",
                "email": "gary.player@gmail.com",
                "first_name": "Gary",
                "last_name": "Player",
                "is_active": true,
                "is_staff": true
            },
            "position": {
                "id": 2,
                "name": "Back-end Developer",
                "level": "Junior",
                "sort": 0
            },
            "phone_number": "0837788876",
            "email": "gary.player@gmail.com",
            "github_user": "Gary",
            "birth_date": "1990-08-09",
            "gender": "M",
            "race": "W",
            "years_worked": 1,
            "age": 28,
            "days_to_birthday": 309
        }
]''')
