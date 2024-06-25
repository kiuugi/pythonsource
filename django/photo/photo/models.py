from django.db import models


# Create your models here.
# 상속받기
class Photo(models.Model):
    # html에서 text로 받는 애들
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=200)

    # html에서 textarer로 받는 애들 textArer
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.title
