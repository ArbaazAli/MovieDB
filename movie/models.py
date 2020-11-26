from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=50)
    confirm_password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Genre(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=30)
    genre = models.ManyToManyField(Genre)
    duration = models.TimeField(auto_now=False, auto_now_add=False)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    thumbnail = models.ImageField(upload_to='thumbnail/')
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    description = models.TextField()

    def __str__(self):
        return self.title

