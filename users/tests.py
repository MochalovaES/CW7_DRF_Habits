from rest_framework.test import APITestCase
from rest_framework import status
from users.models import User


class UserAPITest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(
            name="testuser1",
            email="testuser1@test.com",
            telegram_id="@testtelegram1",
            password='12345'
        )

    def test_create_user(self):
        data = {
            "name": "testuser2",
            "email": "testuser2@test.com",
            "telegram_id": "@testtelegram2",
            "password": "12345"
        }
        response = self.client.post(
            '/create_user/',
            data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )


