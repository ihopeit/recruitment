from django.contrib import admin
from django import forms

from job.models import Job

class JobAdmin(admin.ModelAdmin):
    exclude = ('creator_id','created_date','modified_date')

# Register your models here.
admin.site.register(Job, JobAdmin)