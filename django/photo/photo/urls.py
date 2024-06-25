from django.urls import path
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/photo/
    path("", views.list, name="photo_list"),
    # http://127.0.0.1:8000/photo/new/
    path("new/", views.create, name="photo_create"),
    # http://127.0.0.1:8000/photo/번호/
    path("<int:id>/", views.detail, name="photo_detail"),
    # http://127.0.0.1:8000/photo/remove/번호/
    path("remove/<int:id>/", views.remove, name="photo_remove"),
    # http://127.0.0.1:8000/photo/update/번호/
    path("edit/<int:id>/", views.edit, name="photo_edit"),
]
