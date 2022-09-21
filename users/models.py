from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    second_name = models.CharField(max_length=64)
    age = models.PositiveIntegerField(blank=True, null=True)
    email = models.CharField(
        "email address",
        max_length=256,
        unique=True,
        error_messages={"unique": "A user with that email address already exists."},
    )
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site."
    )
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. \
            Unselect this instead of deleting accounts."
    )

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return f'{self.username} <{self.email}>'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

