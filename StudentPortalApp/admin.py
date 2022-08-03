from django.contrib import admin

# Register your models here.
from StudentPortalApp import models

admin.site.register(models.Login)
admin.site.register(models.Student)

