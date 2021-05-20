from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    birth_date = models.DateField(null=True, blank=True, help_text='Enter in yyyy-mm-dd format')
    contact = models.CharField(max_length=20, help_text='Don\'t enter Country Code')