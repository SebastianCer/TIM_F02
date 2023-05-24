from django.db import models
import datetime



class seller(models.Model):
    name = models.CharField(max_length=50, default="Web")
    address = models.CharField(max_length=150, default="Arequipa")
    phone = models.IntegerField(default='+51 316 243 081')
    date = models.DateField(default=datetime.datetime.date)


class buyer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    phone = models.IntegerField()
    purchase_date = models.DateField(default=datetime.datetime.now)


class producat(models.Model):
    img = models.ImageField(upload_to='media/')
    name = models.CharField(max_length=100)
    dis = models.TextField(max_length=500)
    price = models.CharField(max_length=100)
