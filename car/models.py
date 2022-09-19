from django.db import models

# Create your models here.
class Service(models.Model):
    sname = models.CharField(max_length=50)
    stype= models.CharField(max_length=50)
    price = models.FloatField()
    no_services = models.IntegerField()
    image = models.ImageField(upload_to='images',default='images/img1.jpg')
    description=models.CharField(max_length=1000,default="")
