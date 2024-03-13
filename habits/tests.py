from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habits
from users.models import User


class HabitApiTestCase(APITestCase):
    """
    Тесты на CRUD привычек
    """

    def setUp(self) -> None:
        self.user = User.objects.create(
            name="testuser",
            email="testuser@test.com",
            telegram_id="@testtelegram",
            password='12345'
        )
        self.habit = Habits.objects.create(
            id=1,
            user=self.user,
            place='Дом',
            time="11:00",
            action='Выпить воды',
            is_nice_habit=False,
            periodicity="ежедневно",
            duration_time="00:01",
            reward='Съесть яблоко',
            is_public=True,
        )

    def test_create_habit(self):
        """
        Тестирование создания привычки
        """

        data = {
            "user": self.user.pk,
            "place": "Дом",
            "time": "12:00",
            "action": "Выпить воды",
            "periodicity": "ежедневно",
            "duration_time": "00:01",
            "reward": "Съесть яблоко",
            "is_public": False,
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(
            '/create/',
            data=data)
        self.assertEquals(
            response.status_code,
            status.HTTP_201_CREATED
        )

    def test_list_habit(self):
        """
        Тестирование вывода списка привычек
        """

        self.client.force_authenticate(user=self.user)
        response = self.client.get(
            '/list/')
        self.assertEquals(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_delete_habit(self):
        """
        Тестирование удаления привычки
        """

        self.client.force_authenticate(user=self.user)
        response = self.client.delete(
            '/destroy/1/')
        print(response)
        self.assertEquals(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
