from django.shortcuts import render,redirect
from . models import*
from patient.models import *
# Create your views here.
def patientlist(request):
    doc=Doctor.objects.all()
    doctorid=request.session.get('docid')

    appointment = Appointment.objects.filter(doctor=doctorid)
    return render(request,'doctor/patientlist.html',{'appointments':appointment})
def doctorlogin(request):
    if request.method=='POST':
        name=request.POST['name']
        password=request.POST['password']
        try:
            doctor = Doctor.objects.get(name=name, password=password)
            request.session['docid'] =doctor.id
            return redirect('doctor:patientlist')
        except Doctor.DoesNotExist:
            return render(request,'doctor/doctorlogin.html', {'msg': 'invalid credentials'})
    return render(request,'doctor/doctorlogin.html')
def update_status_of_patient(request,patient_id):
    appointment=Appointment.objects.get(id=patient_id)
    
    appointment.status='confirmed'
    appointment.save()
    return redirect('doctor:patientlist')
def remove_appointment(request,appointment_id):
    Appointment.objects.get(id=appointment_id).delete()
    return redirect('doctor:patientlist')

    