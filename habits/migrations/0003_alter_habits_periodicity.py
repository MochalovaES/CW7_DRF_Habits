# Generated by Django 5.0.3 on 2024-03-13 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habits', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habits',
            name='periodicity',
            field=models.CharField(choices=[('Ежедневно', 'Ежедневно'), ('Каждые ', 'Запущена'), ('Завершена', 'Завершена')], default='ежедневно', max_length=50, verbose_name='Периодичность'),
        ),
    ]
