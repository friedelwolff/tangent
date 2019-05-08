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

    def get_my_profile(self):
        return json.loads(r'''{
  "id": 12,
  "user": {
    "id": 12,
    "username": "pravin.gordhan",
    "email": "pravin@axedmps.com",
    "first_name": "Pravin",
    "last_name": "Gordhan",
    "is_active": true,
    "is_staff": true
  },
  "position": {
    "id": 3,
    "name": "Project Manager",
    "level": "Senior",
    "sort": 0
  },
  "employee_next_of_kin": [
    {
      "id": 4,
      "name": "Mini Ghordan",
      "relationship": "Wife",
      "phone_number": "0827788877",
      "email": "mini@axedmps.com",
      "physical_address": "12 Church Street,\r\nBluekraans,\r\nMidrand,\r\nJohannesburg",
      "employee": 12
    }
  ],
  "employee_review": [
    {
      "id": 9,
      "date": "2016-06-01",
      "salary": "100000.00",
      "type": "S"
    },
    {
      "id": 13,
      "date": "2017-08-30",
      "salary": "120000.00",
      "type": "P"
    }
  ],
  "id_number": "5112125239088",
  "phone_number": "0828899987",
  "physical_address": "12 Church Street,\r\nBluekraans,\r\nMidrand,\r\nJohannesburg",
  "tax_number": "102998766",
  "email": "pravin@axedmps.com",
  "personal_email": "pravin@axedmps.com",
  "github_user": "PravG",
  "birth_date": "1951-12-12",
  "start_date": "2016-06-01",
  "end_date": null,
  "id_document": null,
  "visa_document": null,
  "is_employed": true,
  "is_foreigner": false,
  "gender": "M",
  "race": "B",
  "years_worked": 2,
  "age": 66,
  "next_review": "2018-02-28",
  "days_to_birthday": 69,
  "leave_remaining": "16.50"
}''')

    def github_avatar_url(self, username):
        return None
