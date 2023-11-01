#AbstractUser es una clase que se puede utilizar para personalizar el modelo de usuario predeterminado de Django.
#from django.contrib.auth.models import AbstractUser
from django.db import models

""" class CustomUser(AbstractUser):
    email = models.EmailField(
        max_length=150, unique=True) """
class TUser(models.Model):
    name = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    description = models.TextField()
    active = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)
class TSession(models.Model):
    user = models.ForeignKey(TUser, on_delete=models.CASCADE)
    idstatus = models.IntegerField()
    idrol = models.IntegerField()
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)
class TLogin(models.Model):
    user = models.ForeignKey(TUser, on_delete=models.CASCADE)
    idstatus = models.IntegerField()
    active = models.BooleanField(default=True)
    createdat = models.DateTimeField(auto_now_add=True)
    updatedat = models.DateTimeField(auto_now=True)
    lastrecord = models.CharField(max_length=50)
