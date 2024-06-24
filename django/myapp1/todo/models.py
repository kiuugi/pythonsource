from django.db import models


# Create your models here. (데이터베이스의 테이블 작성)
# 테이블과 동일한 모델 정의(id 자동 삽입함)
class Todo(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    important = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
