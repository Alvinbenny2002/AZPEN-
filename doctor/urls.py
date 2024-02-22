from django.urls import path
from . import views
app_name='doctor'
urlpatterns=[
    path('doctorlogin/',views.doctorlogin,name='doctorlogin'),
    path('patientlist',views.patientlist,name='patientlist')
]