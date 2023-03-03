from django.contrib import admin
from Incident_Management.models import Incident_Data

# Register your models here.

class usernote(admin.ModelAdmin):
    list_display = ('Incident_ID','Incident_Status','user','Incident_Detail','Incident_DT','Incident_Priority')

admin.site.register(Incident_Data,usernote)