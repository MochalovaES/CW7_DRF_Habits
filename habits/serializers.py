from rest_framework import serializers

from habits.models import Habits
from habits.validators import HabitValidator, TimeValidator, ConnectedHabitValidator, NiceHabitValidator


class HabitsSerializer(serializers.ModelSerializer):
    """
    Сериализатор модели Пользователя
    """

    class Meta:
        model = Habits
        fields = '__all__'
        validators = [HabitValidator(field1='reward', field2='habits'),
                      TimeValidator(field1='duration_time'),
                      ConnectedHabitValidator(field1='habits'),
                      NiceHabitValidator(field1='is_nice_habit',
                                         field2='reward',
                                         field3='habits')]
