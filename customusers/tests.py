from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status


class CreateUsersTestCase(APITestCase):

    def test_fail_create_user(self):
        data = {
            "email": "some@mail.com",
            "password": "somepassword"
        }
        response = self.client.post(reverse("signup"), data)        
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_user(self):
        data = {
            "email": "some@mail.com",
            "password": "Somepassword!1"
        }
        response = self.client.post(reverse("signup"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
