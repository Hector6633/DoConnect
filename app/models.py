from django.db import models

# Create your models here.
class Contact_Info(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=False, null=False)
    number = models.CharField(max_length=10)
    message = models.TextField()
    date_time = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
class Appointment(models.Model):
    full_name = models.CharField(max_length=30)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=10)
    service = models.CharField(max_length=30)
    appointment_date = models.DateField()
    appointment_time = models.CharField(max_length=10)
    special_request = models.TextField()
    booked_date_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('appointment_date', 'appointment_time', 'service')
    
    def __str__(self):
        return self.full_name