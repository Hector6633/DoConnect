from django.contrib import admin
from . models import *

class ContactInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    
class AppointmentInfo(admin.ModelAdmin):
    list_display = ('full_name', 'email', 'mobile_number', 'service', 'appointment_date', 'appointment_time', 'special_request', 'booked_date_time')
    readonly_fields = ('booked_date_time',)

admin.site.register(Contact_Info, ContactInfoAdmin)
admin.site.register(Appointment, AppointmentInfo)