from datetime import timedelta

from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):
    """
    Создание модели Привычек
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    place = models.CharField(max_length=50, verbose_name='Место выполнения')
    time = models.TimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=50, verbose_name='Действие')
    is_nice_habit = models.BooleanField(default=False, verbose_name='Приятная привычка', **NULLABLE)
    related_habit = models.ForeignKey('self', on_delete=models.CASCADE, verbose_name='Связанная привычка', **NULLABLE)
    periodicity = models.CharField(default='ежедневно', max_length=50, verbose_name='Периодичность')
    reward = models.CharField(max_length=50, **NULLABLE, verbose_name='Вознаграждение')
    duration_time = models.TimeField(verbose_name='Время на выполнение')
    is_public = models.BooleanField(default=False, verbose_name='Признак публичности')

    def __str__(self):
        return f'{self.user} - {self.action}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
