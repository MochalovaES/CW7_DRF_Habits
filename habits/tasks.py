import os
from celery import shared_task
from datetime import timedelta

from django.utils import timezone

from habits.models import Habits
from habits.services import send_message


@shared_task
def send_notification():  # Функция отправки уведомления
    time_now = timezone.now()
    habits = Habits.objects.all()

    for habit in habits:
        if habit.time >= time_now - timedelta(minutes=15):
            message = f"Напоминание о привычке {habit.action}\n" \
                      f"После этого можно:\n \
                      {habit.habits if habit.habits else habit.reward}"
            send_message(chat_id=habit.user.chat_id,
                         message=message)
