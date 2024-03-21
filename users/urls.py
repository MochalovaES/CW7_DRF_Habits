from users.views import UserCreateAPIView
from users.apps import UsersConfig
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = UsersConfig.name

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # создание токена
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # обновление токена
    path('user/create/', UserCreateAPIView.as_view(), name='user_create'),  # создание пользователя
]
