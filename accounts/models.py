from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class shopper(AbstractUser):
    groups = models.ManyToManyField('auth.Group', related_name='custom_shopper_groups')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='custom_shopper_user_permissions')
    
