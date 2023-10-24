from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.


class User(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    password = models.CharField(max_length=10, validators=[MinLengthValidator(6)])

class Invoices(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=200)
    date = models.DateField()

class Items(models.Model):
    invoice = models.ForeignKey(Invoices, on_delete=models.CASCADE, related_name="items")
    desc = models.TextField()
    rate = models.FloatField()
    quantity = models.IntegerField()

