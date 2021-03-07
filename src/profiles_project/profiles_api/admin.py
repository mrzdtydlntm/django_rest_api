from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.UserProfile)
#pass in our model to register with django admin