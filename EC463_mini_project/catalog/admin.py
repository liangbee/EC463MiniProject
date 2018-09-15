from django.contrib import admin
from catalog.models import HouseRoom,Profile

admin.site.register(HouseRoom)

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

admin.site.site_header='EC463 MiniProject Admin Site'

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profile'

 class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)   
    
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
