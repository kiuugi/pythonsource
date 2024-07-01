from django.db import models
from django.contrib.auth.models import User


# Create your models
# auto_now_add : 가장 처음 삽입시에만 날짜와 시간 삽입
# auto_now : 수정할 때마다 날짜와 시간 변경


class Question(models.Model):
    subject = models.CharField(max_length=200, verbose_name="제목")
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정")
    voter = models.ManyToManyField(
        User, related_name="voter_question"
    )  # author 에서 같은 User를 사용하기 때문에 구별할 이름을 붙여줘야함
    # M:N의 관계이기 때문에 따로 테이블을 만들어줌
    # 하지만 따로 테이블을 만든것은 아니기때문에 여기서는 Question.vote를 통해서 들어가야함
    view_cnt = models.BigIntegerField(default=0)

    def __str__(self) -> str:
        return self.subject


class QuestionCount(models.Model):
    ip = models.CharField(max_length=30)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __unique__(self):
        return self.ip


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    voter = models.ManyToManyField(User, related_name="voter_answer")

    def __str__(self) -> str:
        return self.content


# 댓글
class Comment(models.Model):
    content = models.TextField(verbose_name="내용")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="작성일시")
    modified_at = models.DateTimeField(null=True, blank=True, verbose_name="수정일시")
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, null=True, blank=True
    )
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True, blank=True)
