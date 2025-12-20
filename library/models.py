from django.db import models
from django.contrib.auth.models import User

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Description(models.Model):
#     name = models.CharField(max_length=200)
#
#     def __str__(self):
#         return self.name
#
#
# class Cover(models.Model):
#     image = models.ImageField(upload_to='covers/')
#
#     def __str__(self):
#         return self.image.name

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    description = models.TextField(default='Нет описания')
    cover = models.ImageField(upload_to='covers/', blank=True, null=True)

    def __str__(self):
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')

    RATING_CHOICES = (
        (1, 'Ужасно'),
        (2, 'Плохо'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отлично'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES, default=5)
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('book', 'user')
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.book.title} - {self.rating} ({self.user.username})'