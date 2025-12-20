
from django.db import models
from django.forms import CharField



class Book(models.Model):
    slug=models.SlugField(unique=True, blank=False, null=False)
    name=models.CharField(max_length=100, null=False, blank=False)
    author=models.CharField(max_length=100)
    genre=models.CharField(max_length=100)
    year=models.CharField(max_length=100)

    def __str__(self):
        return self.name

