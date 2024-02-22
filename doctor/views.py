from django.shortcuts import render

# Create your views here.
def patientlist(request):
    return render(request,'doctor/patient.html')
def doctorlogin(request):
    return render(request,'doctor/doctorlogin.html')
    