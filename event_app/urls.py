from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('events/', views.events, name='events'),
    path('vendor/', views.vendor, name='vendor'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('base/', views.base, name='search'),
    path('payment/', views.process_payment, name='process_payment'),
    
    
    
]