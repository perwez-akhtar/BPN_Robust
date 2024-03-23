from django.conf import settings
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.contrib.auth.models import *
from django.core.mail import send_mail


from django.http import HttpResponse

from home.models import *

def base(request):
  return render(request,'base.html') 

# @send_mail
def user_register(request): 
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        mobile = request.POST.get('mobile')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if a user with the provided username already exists
        existing_user = User.objects.filter(username=username)

        if existing_user:
            # login(request, existing_user)
            messages.success(request, "User already register .")
            return redirect('user_register')  # Redirect to the index page after successful login
        
        else:
            # Create a new user
            user = User.objects.create_user(username=username, password=password)
            user.full_name = fullname
            user.mobile = mobile
            user.save()

            # Log in the newly created user
            login(request, user)
            messages.success(request, "Account created and logged in successfully.")
            return redirect('index')  # Redirect to the index page after successful creation and login

    # Render the registration form template for GET requests
    return render(request, 'user_register.html')

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "Login successfull.")
            return render(request,'index.html')
            
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return redirect('user_register')  
    else:
        return render(request, 'user_register.html')

def user_logout(request):
    logout(request)
    return redirect('/')




def index(request):
  return render(request,'index.html')    
def about(request):
  return render(request,'about.html')    
def service(request):
  return render(request,'service.html')    
def team(request):
  return render(request,'team.html')    
def contact(request):
  return render(request,'contact.html')   

def appointment(request):
  doc=Doctor.objects.all()
  return render(request,'appointment.html',{'doc': doc})   

def dashboard(request):
  return render(request,'dashboard.html')
def adminpanel(request):
  
  doctors = Appointment.objects.all()
  return render(request, 'adminpanel.html', {'doctors': doctors})


from django.shortcuts import render, redirect
from .models import Patient

def patient_form(request):
    if request.method == 'POST':
        
        doctor = request.POST.get('doctor')
        name = request.POST.get('name')
        date = request.POST.get('date')
        time = request.POST.get('time')

        
        patient = Appointment(name=name, doctor=doctor, appointment_date=date, appointment_time=time)
        patient.save()
        
        return redirect('appointment') 

    return render(request, 'appointment.html')



def sendemailtoclient():
    subject="Message testing of email from Perwez"            
    messages="Testing for the reminder for Appointment"
    from_email=settings.EMAIL_HOST_USER
    recipient_list=["perwezakhtar29@gmail.com"]
    send_mail(subject,messages,from_email,recipient_list)

def send_email(request):
    sendemailtoclient()
    return redirect('/')    
    