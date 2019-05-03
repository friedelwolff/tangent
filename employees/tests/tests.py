from django.test import TestCase, override_settings
from django.test.client import Client


class TestURLS(TestCase):

    def setUp(self):
        self.client = Client()

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
