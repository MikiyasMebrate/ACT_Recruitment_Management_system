from django.contrib import admin
from . import models
# Register your models here.


admin.site.register(models.Candidate)
admin.site.register(models.Education)
admin.site.register(models.Experience)
admin.site.register(models.Skill)
admin.site.register(models.Social_media)
admin.site.register(models.Department)
admin.site.register(models.Job_Type)
admin.site.register(models.Job_Posting)
admin.site.register(models.Application)
admin.site.register(models.Interviews)
admin.site.register(models.Notes)