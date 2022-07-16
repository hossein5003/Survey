from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Email=models.EmailField(unique=True)
    Username=models.CharField(max_length=15)
    Password=models.CharField(max_length=20)


class Respondent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Respondent_id = models.CharField(max_length=15, unique=True)


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Admin_id = models.CharField(max_length=15, unique=True)