from django.urls import path
from . import views
app_name='patient'
urlpatterns=[
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('booking/',views.booking,name='booking'),
    path('',views.home,name='home'),
    path('list/',views.list,name='list')
    
]