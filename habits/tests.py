from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitApiTestCase(APITestCase):
    """ Тесты на CRUD привычек"""

    def setUp(self):
        self.user = User.objects.create(
            name="testuser",
            email="testuser@test.com",
            telegram_id="@testtelegram",
            password='12345'
        )
        self.habit = Habits.objects.create(
            id=10,
            user=self.user,
            place='Дом',
            time='11:42',
            action='Выпить воды',
            is_nice_habit=False,
            periodicity='daily',
            duration_time='00:01',
            reward='Съесть яблоко',
            is_public=True,
        )

    def test_create_habits(self):
        """ Тестирование создания привычки"""

        data = {
            "user": self.user.pk,
            "place": "Дом",
            "time": "11:42",
            "action": "Выпить воды",
            "reward": "Съесть яблоко",
            "periodicity": "daily",
            "is_public": False,
            "duration_time": "00:01",
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/create/',
            data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habits(self):
        """ Тестирование вывода списка привычек """

        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/list/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_habits(self):
        """Тестирование вывода одной привычки"""

        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/retrieve/10/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_habits(self):
        """Тестирование редактирования привычки """

        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/update/10/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habits(self):
        """Тестирование удаления привычки"""

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            '/destroy/10/')
        print(response)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

    def test_list_public_habits(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/list_public/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )
