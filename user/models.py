from django.db import models
from django.utils import *
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class CustomAccountManager(BaseUserManager):

    def create_user(self, id_number, name, birth_date, participant_type, password, **other_fields):
        user = self.model(id_number=id_number, name=name, birth_date=birth_date, participant_type=participant_type, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, id_number, name, birth_date, participant_type, password, **other_fields):
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_active', True)

        return self.create_user(id_number, name, birth_date, participant_type, password, **other_fields)


class NewUser(AbstractBaseUser, PermissionsMixin):
    
    id_number = models.CharField(max_length=6, unique=True, primary_key=True)

    PARTICIPANT_TYPES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('faculty', 'Faculty'),
    )

    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    department = models.CharField(max_length=200)
    participant_type = models.CharField(choices=PARTICIPANT_TYPES, max_length=20)

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()
    
    USERNAME_FIELD = 'id_number' # Let the ID number be the user's username and primary key.
    REQUIRED_FIELDS = ['name', 'birth_date', 'department', 'participant_type']

    def __str__(self):
        return self.name + ' (' + self.participant_type + ')'
