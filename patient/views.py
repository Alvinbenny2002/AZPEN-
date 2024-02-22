from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'patient/home.html')
def booking(request):
    return render(request,'patient/booking.html')
def login(request):
    return render(request,'patient/login.html')
def signup(request):
    return render(request,'patient/signup.html')
def list(request):
    return render(request,'patient/list.html')