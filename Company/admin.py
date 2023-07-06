from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Blog_Categories)
admin.site.register(models.Blog)
admin.site.register(models.Comment)