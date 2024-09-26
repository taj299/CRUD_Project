from django.contrib import admin

from .models import UserProfile

#we will make a model admin class
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','password')