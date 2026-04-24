from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def booking(request):
    if request.method == 'POST':
        try:
            full_name = request.POST.get('full_name')
            email = request.POST.get('email')
            mob_number = request.POST.get('mob_number')
            service = request.POST.get('service')
            appointment_date = request.POST.get('appointment_date')
            appointment_time = request.POST.get('appointment_time')
            special_request = request.POST.get('special_request')
            
            conflict = Appointment.objects.filter(
                appointment_date=appointment_date,
                appointment_time=appointment_time,
            ).exists()

            if conflict:
                error_msg = 'This time slot is already booked. Please choose another.'
                messages.error(request, error_msg)
                return redirect('booking')
            else:
                appointment_data = Appointment.objects.create(full_name=full_name, email=email, mobile_number=mob_number, service=service, appointment_date=appointment_date, appointment_time=appointment_time, special_request=special_request)
                appointment_data.save()
                success_msg = 'Appointment Booked Successfully'
                messages.success(request, success_msg)
                return redirect('booking')
        except Exception as e:
            error_msg = 'Something went wrong!'
            messages.error(request, error_msg)
            return redirect('booking')
    return render(request, 'booking.html')

def contact(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            number = request.POST.get('number')
            message = request.POST.get('message')
            customer_contact_data = Contact_Info.objects.create(name=name, email=email, number=number, message=message)
            customer_contact_data.save()
            success_msg = 'Registered'
            messages.success(request, success_msg)
            return redirect('contact')
        except Exception as e:
            error_msg = '500 Error!'
            messages.error(request, error_msg)
            return redirect('contact')
    return render(request, 'contact.html')