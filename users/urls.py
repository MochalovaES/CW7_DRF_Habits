from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView

app_name = UsersConfig.name


urlpatterns = [
    path('create_user/', UserCreateAPIView.as_view(), name='create_user')
]