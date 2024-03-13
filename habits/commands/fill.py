from django.core.management import BaseCommand
from habits.models import Habits

data = [
    {
        "id": 1,
        "user_id": 1,
        "place": "Дом",
        "time": "12:00",
        "action": "Выпить воды",
        "periodicity": "ежедневно",
        "duration_time": "00:01",
        "reward": "Съесть яблоко",
        "is_public": False,
    },
    {
        "id": 2,
        "user_id": 1,
        "place": "Дом",
        "time": "7:00",
        "action": "Проснуться",
        "periodicity": "ежедневно",
        "duration_time": "00:01",
        "reward": "Выпить кофе",
        "is_public": False,
    },
    {
        "id": 3,
        "user_id": 1,
        "place": "Работа",
        "time": "15:00",
        "action": "Съесть творог",
        "periodicity": "ежедневно",
        "duration_time": "00:15",
        "reward": "Съесть банан",
        "is_public": False,
    },
]


class Command(BaseCommand):
    """Добавление данных в БД"""

    def handle(self, *args, **options):
        habits_list = data
        Habits.objects.all().delete()

        for habits in habits_list:
            Habits.objects.create(**habits)
