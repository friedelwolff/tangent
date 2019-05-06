from datetime import date

from django.test import TestCase, override_settings
from django.test.client import Client

from employees import views


@override_settings(MOCK_API=True)
class TestURLS(TestCase):

    def setUp(self):
        self.client = Client()

    def login(self):
        self.client.login(username="pravin.gordhan", password="pravin.gordhan")

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Log in")

    def test_login(self):
        response = self.client.get('/auth/login/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Username")

        response = self.client.post('/auth/login/', follow=True, data={
            "username": "x",
            "password": "x",
        })
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Log in")
        self.assertNotContains(response, "Log out")

        response = self.client.post('/auth/login/', follow=True, data={
            "username": "pravin.gordhan",
            "password": "pravin.gordhan",
        })
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, "Log in")
        self.assertContains(response, "Log out")

    def test_employee_list(self):
        #Test unauthenticated:
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/list/', follow=True)
        self.assertContains(response, "Password")

        #Test authenticated:
        self.login()
        response = self.client.get('/list/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Github")

    def test_statistics(self):
        #Test unauthenticated:
        response = self.client.get('/statistics/')
        self.assertEqual(response.status_code, 302)
        response = self.client.get('/statistics/', follow=True)
        self.assertContains(response, "Password")

        #Test authenticated:
        self.login()
        response = self.client.get('/statistics/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Upcoming birthdays")


def TestHelpers(TestCase):

    def test_birthday_filtering(self):
        stats_view = views.EmployeeStatsView()
        # We set 'today' explicitly so that we can test against a fixed
        # reference point:
        stats_view.today = date.fromisoformat('1919-05-06')
        self.assertTrue(stats_view._date_soon('2010-05-06'))
        self.assertTrue(stats_view._date_soon('2000-05-07'))
        self.assertTrue(stats_view._date_soon('1990-06-01'))
        self.assertFalse(stats_view._date_soon('1970-07-01'))
        self.assertFalse(stats_view._date_soon('1960-05-01'))
