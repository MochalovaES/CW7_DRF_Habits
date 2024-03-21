from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginations import HabitsPagination
from users.permissions import IsUser
from habits.serializers import HabitsSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """
    Создание привычки
    """
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    # Функция привязывает автора к его привычке
    def perform_create(self, serializer):
        new_habit = serializer.save()
        new_habit.user = self.request.user
        new_habit.save()


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """
    Просмотр одной привычки
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsUser]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """
    Редактирование привычки
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """
    Удаление привычки
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsUser]


class HabitListAPIView(generics.ListAPIView):
    """
    Список привычек
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all()
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated, IsUser]

    def get_queryset(self):
        list_habits = super().get_queryset()
        return list_habits.filter(user=self.request.user)


class HabitPublicAPIView(generics.ListAPIView):
    """
    Список публичных привычек
    """
    serializer_class = HabitsSerializer
    queryset = Habits.objects.all().filter(is_public=True)
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]
