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


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name
