from django.db import models


# Create your models here.
"""
class Book (models.Model):
    title = models.CharField(max_length = 256)
    pageCount = models.IntegerField(default = 0)
    imageUrl = models.CharField(max_length = 256, null = True)
    shortDescription = models.CharField(max_length = 256, null = True)
    longDescription = models.TextField(null = True)
    authors = models.CharField(max_length = 200, null = True)
    status = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return f"{self.id} {self.title}"

class Review(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now = True)
    book_id = models.BigIntegerField(default = 1)   """

from django.contrib.auth.models import User



class Author(models.Model):
    name = models.CharField(max_length = 256)
    created_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.name


class Book (models.Model):
    title = models.CharField(max_length = 256)
    pageCount = models.IntegerField(default = 0)
    shortDescription = models.CharField(max_length = 256, null = True)
    longDescription = models.TextField(null = True)
    status = models.CharField(max_length = 200, null = True)
    author = models.ManyToManyField(Author)
    image = models.ImageField(upload_to = "bookImages", null = True)

    def __str__(self):
        return f"{self.id} {self.title}"



class Review(models.Model):
    body = models.TextField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null = True)
    created_at = models.DateTimeField(auto_now = True)
    book = models.ForeignKey(Book, on_delete = models.CASCADE, null = True)
    image = models.ImageField(upload_to = "bookImages/review", null = True)