from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.process_payment, name='process_payment'),
]
