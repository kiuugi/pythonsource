from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    # http://127.0.0.1:8000/board/
    path("", views.question_list, name="question_list"),
    # http://127.0.0.1:8000/board/1/
    path("<int:qid>/", views.question_detail, name="question_detail"),
    # http://127.0.0.1:8000/board/question/create/
    path("question/create/", views.question_create, name="question_create"),
    # http://127.0.0.1:8000/board/answer/create/1/
    path("answer/create/<int:qid>/", views.answer_create, name="answer_create"),
    # http://127.0.0.1:8000/board/question/modify/1/
    path(
        "question/modify/<int:qid>/",
        views.question_modify,
        name="question_modify",
    ),
    path(
        "question/delete/<int:qid>/",
        views.question_delete,
        name="question_delete",
    ),
    path(
        "answer/modify/<int:aid>/",
        views.answer_modify,
        name="answer_modify",
    ),
    path(
        "answer/delete/<int:aid>/",
        views.answer_delete,
        name="answer_delete",
    ),
    path(
        "comment/create/question/<int:qid>/",
        views.comment_create_question,
        name="comment_create",
    ),
    path(
        "comment/modify/question/<int:cid>/",
        views.comment_modify_question,
        name="comment_modify",
    ),
    path(
        "comment/delete/question/<int:cid>/",
        views.comment_delete_question,
        name="comment_delete",
    ),
    path(
        "comment/create/answer/<int:aid>/",
        views.comment_create_answer,
        name="comment_answer_create",
    ),
    path(
        "comment/modify/answer/<int:cid>/",
        views.comment_modify_answer,
        name="comment_answer_modify",
    ),
    path(
        "comment.delete/answer/<int:cid>/",
        views.comment_delete_answer,
        name="comment_answer_delete",
    ),
    # 추천
    # 질문추천, 답변추천
    # vote/question/번호
    path("vote/question/<int:qid>", views.vote_question, name="vote_question"),
    # vote/answer/번호
    path("vote/answer/<int:aid>", views.vote_answer, name="vote_answer"),
]
