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


class Musician(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    instrument = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name + " " + self.instrument


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()

    def __str__(self) -> str:
        return self.artist.first_name + ", " + self.name


class Fruit(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
