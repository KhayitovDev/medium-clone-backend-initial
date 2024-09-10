from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    date_joined = models.DateField(auto_now_add=True)
    
    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-date_joined']
        
    def __str__(self):
        if self.full_name:
            return self.full_name
        else:
            return self.username or self.email
        
    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name} {self.middle_name}'
    
    
