from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    ROLES = [
        ['ROLES','Roles'],
        ['USER','User'],
        ['MANAGER','Manager']
    ]

    roles = models.CharField(choices=ROLES,default='USER')
    
    @property    # Atributga aylantirib beradi
    def is_admin(self):
        return self.roles == "ADMIN"

    
    @property    # Atributga aylantirib beradi
    def is_roles(self):
        return self.roles == "ROLES"
        
    @property    # Atributga aylantirib beradi
    def is_user(self):
        return self.roles == "USER"
    
    