# Create your models here.
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    groups = models.ManyToManyField(Group, related_name="customuser_groups")  # Fix clash
    user_permissions = models.ManyToManyField(Permission, related_name="customuser_permissions")


