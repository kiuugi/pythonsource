from django.urls import path
from . import views

# config에서 users를 포함시켜서 주소줄에 기본적으로 users/ 가 달림
urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.common_login, name="login"),
    path("", views.index, name="index"),
]
