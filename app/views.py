from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.db import transaction

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
            with transaction.atomic():
                last_token = Appointment.objects.select_for_update().filter(
                    appointment_date=appointment_date,
                    appointment_time=appointment_time
                ).order_by('-token_number').first()

            token_number = 1 if not last_token else last_token.token_number + 1
            # OPTIONAL: Limit patients per slot (e.g., 10)
            # when the value of max_patients is 5 but the value of token_number is 4
            MAX_PATIENTS = 5
            if token_number >= MAX_PATIENTS:
                messages.error(request, "This slot is full. Please choose another time.")
                return redirect('booking')
            # Save appointment with token
            appointment_data = Appointment.objects.create(
                full_name=full_name,
                email=email,
                mobile_number=mob_number,
                service=service,
                appointment_date=appointment_date,
                appointment_time=appointment_time,
                special_request=special_request,
                token_number=token_number   
            )
            appointment_data.save()
            subject = "DoConnect Appointment Confirmation"
            message = f"Dear {full_name},\nYour appointment successfully booked.\nHere is your Appointment Details:\n\tToken Number: {token_number}\n\tFull Name: {full_name}\n\tMobile Number:{mob_number}\n\tService: {service}\n\tAppointment Date: {appointment_date}\n\tAppointment Time: {appointment_time}\nPlease keep this email for your records and do not forward or share any other person.Please arrive before your token number is called.\nBest Regards,\nDoConnect Team"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
            messages.success(request, f'Appointment booked! Your token number is {token_number}')
            return redirect('booking')
        except Exception as e:
            messages.error(request, 'Something went wrong!')
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
            subject = "DoConnect Feedback"
            message = f"Dear {name},\nThank You for your feedback with DoConnect. Our advisor will verify and get in touch with you.\nPlease keep this email for your records and do not forward or share any other person.\nTo get started, please visit our website at https://doconnect.pythonanywhere.com/ and use our services.\nBest Regards, \nDoConnect Team"
            recipient = email
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [recipient],
                fail_silently=True,
            )
            success_msg = 'Registered your Feedback'
            messages.success(request, success_msg)
            return redirect('contact')
        except Exception as e:
            error_msg = '500 Error!'
            messages.error(request, error_msg)
            return redirect('contact')
    return render(request, 'contact.html')