from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()

class IndexTestCase(APITestCase):
    def test_index(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)        
        

class MovieListCreateTestCase(APITestCase):
    def setUp(self):
        self.url = reverse("create")

    def authenticate(self):
        self.client.post(
            reverse("signup"),
            {
                "email": "test@mail.com",
                "password": "Password##!123",
            },
        )

        response = self.client.post(
            reverse("login"),
            {
                "email": "test@mail.com",
                "password": "Password##!123",
            },
        )
        token = response.data["tokens"]["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {token}")


    def test_list_movies(self):

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 0)
        self.assertEqual(response.data["results"], [])

    def test_movies_creation(self):
        self.authenticate()

        sample_data = {
            "name": "movie1",
            "description": "description movie",
            "year": "2023",
            "category": "category",
            "private": 0
            }
            
        response = self.client.post(reverse("create"), sample_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], sample_data["name"])
