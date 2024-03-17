from django.urls import path
from . import views
app_name='doctor'
urlpatterns=[
    path('doctorlogin/',views.doctorlogin,name='doctorlogin'),
    path('patientlist',views.patientlist,name='patientlist'),
    path('update_status_of_patient/<int:patient_id>',views.update_status_of_patient,name='update_status_of_patient'),
    path('remove_appointment/<int:appointment_id>,',views.remove_appointment,name='remove_appointment')
]