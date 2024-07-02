from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.list, name="list"),
    path("post/<int:post_id>/", views.detail, name="detail"),
    path("post/create/", views.create, name="create"),
    path("post/modify/<int:post_id>", views.modify, name="modify"),
    path("post/delete/<int:post_id>", views.delete, name="delete"),
    # 댓글
    path("post/comment/<int:post_id>", views.comment_create, name="comment_create"),
    # 좋아요
    path("post/like/<int:post_id>", views.post_like, name="post_like"),
]
