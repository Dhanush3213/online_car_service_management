from django.db import models
from car.models import Service

# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=35)
    password = models.CharField(max_length=15)
    role = models.IntegerField(default=1)

class User (models.Model):
    loginid=models.ForeignKey(Login,on_delete=models.CASCADE)
    firstname=models.CharField(max_length=20)
    email=models.EmailField()
   
class Order(models.Model):
    user=models.ForeignKey(Login,on_delete=models.CASCADE)
    Service= models.ForeignKey(Service,on_delete=models.CASCADE)
    card_num=models.CharField(max_length=14)
    cvv=models.IntegerField()
    expiry=models.CharField(max_length=7)
    booking_date=models.CharField(max_length=14)
    slots = models.CharField(max_length=10)
    amount=models.FloatField()
    order_date=models.DateField(default='2022-08-18')
    status=models.IntegerField()