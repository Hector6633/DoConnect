from django.contrib import admin
from . models import *

class ContactInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)

admin.site.register(Contact_Info, ContactInfoAdmin)