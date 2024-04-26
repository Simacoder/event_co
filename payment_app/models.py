from django.db import models


# Create your models here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from event_app.models import Payment
from payment_app.models import Payment


from django.db import models

class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

