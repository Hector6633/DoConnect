from django.shortcuts import render
from django.contrib.auth.models import User
from app.models import Appointment, Contact_Info
# Create your views here.

def dashboard_index(request):
    admin = 2
    total_patients = User.objects.all().count()
    total_patients_count = total_patients - admin
    total_appointments = Appointment.objects.all()
    total_feedbacks = Contact_Info.objects.all()
    total_revenue = total_appointments.count() * 250
    total_data = {
        'total_patients': total_patients_count,
        'total_appointments': total_appointments.count(),
        'total_revenue': total_revenue,
        'total_feedbacks': total_feedbacks.count(),
    }
    
    return render(request, 'dashboard/dashboard-index.html', total_data)

def appointments(request):
    total_appointments = {
        'appointments': Appointment.objects.all(),
    }
    return render(request, 'dashboard/appointments.html', total_appointments)

def feedbacks(request):
    total_feedbacks = {
        'feedbacks': Contact_Info.objects.all(),
    }
    return render(request, 'dashboard/contacts.html', total_feedbacks)