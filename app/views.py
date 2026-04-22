from django.shortcuts import render, redirect
from . models import *
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'service.html')

def booking(request):
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