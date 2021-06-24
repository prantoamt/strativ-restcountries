from django.db import models
from django.contrib.auth.models import AbstractUser, Group
import uuid

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(db_column='user_id', primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(db_column='first_name', max_length=64, null=True, blank=True)
    last_name = models.CharField(db_column='last_name', max_length=64, null=True, blank=True)
    username = models.CharField(db_column='username', unique=True, max_length=64)
    password = models.CharField(db_column='password', max_length=256)

    @property
    def fullname(self) -> str:
        if self.first_name and self.last_name:
            return self.first_name + ' ' + self.last_name
        else:
            return self.username

    def __str__(self) -> str:
        return self.username

    class Meta:
        verbose_name_plural = 'Users'
        db_table = 'User'


class CustomGroup(Group):
    class Meta:
        proxy = True
        app_label = 'administrations'
        verbose_name = 'Group'


