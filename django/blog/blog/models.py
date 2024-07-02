from django.db import models
from django.contrib.auth.models import User

from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True, upload_to="image")
    created_at = models.DateTimeField(auto_now_add=True)  # 처음 한번만
    modified_at = models.DateTimeField(auto_now=True)  # 수정 할 때마다
    # 따로 테이블이 만들어지는 칼럼들
    likes = models.ManyToManyField(User, related_name="likes", blank=True)
    tags = TaggableManager()

    # 리스트 추출 시 작성일자의 내림차순으로 추출
    class Meta:
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    """
    user, post, content, created_at, modified_at
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # admin 사이트에서 보여주는 방식(admin.py 에서도 변경가능)
    def __str__(self) -> str:
        return "%s - %s" % (self.id, self.user)
