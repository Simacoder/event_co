from django.shortcuts import render
from .models import Payment
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from django.db import models


def process_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            payment = Payment.objects.create(amount=amount)
            return JsonResponse({'success': True, 'message': 'Payment processed successfully'})
    return JsonResponse({'success': False, 'message': 'Payment failed'})
