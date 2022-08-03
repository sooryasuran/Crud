from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_student = models.BooleanField(default=False)

class Student(models.Model):
    user = models.ForeignKey(Login,on_delete=models.CASCADE,related_name='student')
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Email_id = models.EmailField(max_length=250)
    Phone = models.CharField(max_length=50)
    Address1 = models.CharField(max_length=500)
    Address2 = models.CharField(max_length=500)




