from django.contrib import admin
from profiles_api import models

# Register your models here.

admin.site.register(models.UserProfile) #register UserProfile model with admin site
admin.site.register(models.ProfileFeedItem) #register ProfileFeedItem model with admin site
