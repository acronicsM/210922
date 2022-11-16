from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models
from django.utils import timezone

from users.models import User


class Project(models.Model):
    name = models.CharField(max_length=64)
    link = models.URLField(max_length=512)
    users = models.ManyToManyField(User)

    def __str__(self):
        return f'{self.name} <{self.link}> [{self.users}]'


class TodoProject(models.Model):
    project = models.OneToOneField(Project, on_delete=models.CASCADE)
    text = models.TextField()
    date_create = models.DateTimeField(default=timezone.now)
    date_update = models.DateTimeField(default=timezone.now)
    activ = models.BooleanField()
    user = models.ForeignKey(User, models.PROTECT)
