from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        try:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            user_create = User.objects.create_user(username=username, email=email, password=password)
            user_create.save()
            subject = "DoConnect Account Created"
            message = f"Dear {username},\nThank You for creating an account with DoConnect. Your account has been created successfully.\nPlease keep this email for your records and do not forward or share any other person.\nTo get started, please visit our website at https://doconnect.pythonanywhere.com/ and use our services.\nBest Regards,\nDoConnect Team"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=True,
            )
            success_msg = 'Account Created'
            messages.success(request, success_msg)
            return redirect('sign_in')
        except Exception as e:
            error_msg = '500 Error!'
            messages.error(request, error_msg)
            return redirect('sign_up')
    return render(request, 'sign-up.html')

def sign_in(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_auth = authenticate(request, username=username, password=password)
        if user_auth is not None:
            login(request, user_auth)
            return redirect('index')
        else:
            error_msg = 'Invalid Credentials'
            messages.error(request, error_msg)
            return redirect('sign_in')
    return render(request, 'sign-in.html')

@login_required(login_url='sign_in')
def sign_out(request):
    logout(request)
    return redirect('sign_in')