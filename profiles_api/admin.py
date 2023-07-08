from django.contrib import admin
from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile) #register UserProfile model with admin site

