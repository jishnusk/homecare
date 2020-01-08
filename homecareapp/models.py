from django.db import models
class Login(models.Model):
    email    = models.CharField(max_length=30)
    password = models.CharField(max_length=30) 
class Prosignup(models.Model):
    name = models.CharField(max_length=30)
    gender = models.CharField(max_length=30)
    mobile = models.IntegerField(10) 
    pincode = models.IntegerField(6) 
    experience = models.IntegerField(2) 
    website = models.CharField(max_length=30)
    expertin = models.CharField(max_length=30)
    Fk_Login = models.ForeignKey(Login,on_delete=models.CASCADE)
class Customersignup(models.Model):
    name = models.CharField(max_length=30)
    mobile = models.IntegerField(10) 
    pincode = models.IntegerField(6)
    Fk_Login = models.ForeignKey(Login,on_delete=models.CASCADE)