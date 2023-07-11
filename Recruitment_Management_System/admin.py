from django.contrib import admin
from . import models
# Register your models here.
class MyModelAdmin(admin.ModelAdmin):
    search_fields = ['title']

admin.site.register(models.Skill, MyModelAdmin)
admin.site.register(models.Candidate)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Department)
admin.site.register(models.Job_Type)
admin.site.register(models.Job_Posting)
admin.site.register(models.Application)
admin.site.register(models.Interviews)
admin.site.register(models.Notes)