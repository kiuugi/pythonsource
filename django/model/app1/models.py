from django.db import models


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        db_table = "person"

    # makemigrations 대상 아님
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
