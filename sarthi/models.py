from django.db import models
from isbn_field import ISBNField


# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=100)
    isbn = ISBNField()
    author = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    number_of_pages = models.IntegerField()
    publisher = models.CharField(max_length=100)
    release_date = models.DateField(max_length=100)
