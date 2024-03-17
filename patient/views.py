from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def home(request):
    return render(request,'patient/home.html')
def booking(request):
    doctors=Doctor.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        date=request.POST['date']
        time=request.POST['time']
        message=request.POST['message']
        doctor_id=request.POST['doctor']
        doctor=Doctor.objects.get(id=doctor_id)
        appointment=Appointment(name=name,date=date,time=time,doctor=doctor,message=message,status='waiting')
        appointment.save()
        return render(request,'patient/booking.html',{'msg':'your Appointment updation will be added in APPOINTMENT LIST'})
    return render(request,'patient/booking.html',{'doctors':doctors})
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Patient.objects.filter(email=email,repass=password).exists():
            return render(request,'patient/booking.html')
        else:
            return render(request,'patient/login.html',{'msg':'invalid email or password?'})
    return render(request,'patient/login.html')
def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        patient=Patient(name=name,email=email,repass=password)
        patient.save()
        return redirect('patient:login')
    return render(request,'patient/signup.html')
def list(request):
    patient=Appointment.objects.filter(status='confirmed')
    return render(request,'patient/list.html',{'patient':patient})