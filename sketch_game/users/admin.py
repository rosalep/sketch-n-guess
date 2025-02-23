from django.contrib import admin
from .models import CustomUser, Profile
# Register your models here.
admin.site.register(CustomUser) # allows CustomUser to be used
admin.site.register(Profile)