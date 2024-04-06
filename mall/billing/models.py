from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    is_trusted = models.BooleanField(default=False)


class Customer(models.Model):
    name = models.TextField(max_length=50)
    number = models.TextField(max_length=15)

    def __str__(self):
        return f"{self.name}"
    

class Product(models.Model):
    item_name = models.TextField(max_length=25)
    cost = models.IntegerField()

    def __str__(self):
        return f"{self.item_name}"
    

class Sale(models.Model):
    sold_by = models.ForeignKey(User, on_delete=models.PROTECT)
    item = models.ForeignKey(Product, on_delete=models.PROTECT)
    buyer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.sold_by} sold {self.quantity} {self.item} to {self.buyer}"