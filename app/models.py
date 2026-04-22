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