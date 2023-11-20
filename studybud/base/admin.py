

# from django.contrib import admin

# # Register your models here.

# from .models import Room, Topic, Message, User


# admin.site.register(User)
# admin.site.register(Room)
# admin.site.register(Topic)
# admin.site.register(Message)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Room, Topic, Message, User

class CustomUserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'name', 'is_staff')
    # Customize other fields and options as needed

admin.site.register(User, CustomUserAdmin)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
