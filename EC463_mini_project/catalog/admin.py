from django.contrib import admin
from catalog.models import HouseRoom,Profile

admin.site.register(HouseRoom)


from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


