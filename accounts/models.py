from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = [
        ['ROLES','Roles'],
        ['USER','User'],
        ['MANAGER','Manager']
    ]

    roles = models.CharField(choices=ROLES,default='USER')
    
