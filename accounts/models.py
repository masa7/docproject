from django.db import models

# Create your models here.
# import AbstractUser class
from django.contrib.auth.models import AbstractUser
class CustomUser(AbstractUser):
    '''
    custom user model based on AbstructUser model
    '''
    pass 