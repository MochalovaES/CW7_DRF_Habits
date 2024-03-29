# Generated by Django 5.0.3 on 2024-03-10 16:50

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Habits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=50, verbose_name='Место выполнения')),
                ('time', models.TimeField(verbose_name='Время выполнения')),
                ('action', models.CharField(max_length=50, verbose_name='Действие')),
                ('is_nice_habit', models.BooleanField(blank=True, default=False, null=True, verbose_name='Приятная привычка')),
                ('periodicity', models.CharField(choices=[('Создана', 'Создана'), ('Запущена', 'Запущена'), ('Завершена', 'Завершена')], default='ежедневно', max_length=50, verbose_name='Периодичность')),
                ('reward', models.CharField(blank=True, max_length=50, null=True, verbose_name='Вознаграждение')),
                ('duration_time', models.DurationField(default=datetime.timedelta(seconds=120), verbose_name='Время на выполнение')),
                ('is_public', models.BooleanField(default=False, verbose_name='Признак публичности')),
                ('related_habit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='habits.habits', verbose_name='Связанная привычка')),
            ],
            options={
                'verbose_name': 'Привычка',
                'verbose_name_plural': 'Привычки',
            },
        ),
    ]
