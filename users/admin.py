from django.contrib import admin

from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

admin.site.register(User)
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     list_display = ["id", "username", "email", "is_active", "is_staff"]
#     ordering = ["-username"]
#
#     class Meta:
#         model = User

