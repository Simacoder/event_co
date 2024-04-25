from django.db import models

# Create your models here.
class Event(models.Model):
    img= models.ImageField(upload_to="pic")
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=50)
    def __str__(self):
        return self.name



class Booking(models.Model):
    cus_name=models.CharField(max_length=55)
    cus_cell=models.CharField(max_length=12)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)

class Vendoring(models.Model):
    require = models.CharField(max_length=200,null=True)
    description = models.TextField()
    start_time = models.DateField()
    end_time = models.TimeField()