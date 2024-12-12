from django.db import models

# Create your models here.
class SignUp(models.Model):
    user_name = models.CharField(max_length=30)
    email = models.EmailField()
    password_one = models.CharField(max_length=128)  
    password_two = models.CharField(max_length=128)  