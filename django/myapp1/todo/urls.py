from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/todo/ == ""
    path("", views.list, name="list"),
    # http://127.0.0.1:8000/todo/ == "create"
    # views.create views 에 있는 함수명과 맞춰줌
    path("create/", views.create, name="create"),
    # http://127.0.0.1:8000/todo/글 번호
    path("<int:id>/", views.read, name="read"),
    # http://127.0.0.1:8000/todo/done/글 번호
    path("done/<int:id>/", views.done, name="done"),
    # http://127.0.0.1:8000/todo/done/
    path("done/", views.done_list, name="done_list"),
    # http://127.0.0.1:8000/todo/edit/글 번호
    path("edit/<int:id>", views.edit, name="edit"),
]
