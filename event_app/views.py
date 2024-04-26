import datetime
from http import client
import square
from square.client import Client
from django.core.mail import send_mail
from django.shortcuts import render, redirect, HttpResponse
from . models import Event
from .models import Payment
from . forms import BookingForm
from . vendorform import BookingFormv
from .contact_form import ContactForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt



from django.template.loader import render_to_string

scopes = ['https://www.googleapis.com/auth/calendar']

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    dict_eve={
        'eve':Event.objects.all()
    }
    return render(request, 'events.html', dict_eve)

def vendor(request):
    form = BookingFormv(request.POST)

    if request.method == 'POST':
        form=BookingFormv(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        
        form=BookingFormv()
        context={
        'form':form
        }
        req = request.POST['req']
        start = request.POST['start']
        time = request.POST['time']
        email = request.POST['email']
        starts = start +' '+ time +':' '00'
    
        start_time = datetime.datetime.strptime(starts,"%Y-%m-%d %H:%M:%S")
        end_time  = start_time + datetime.timedelta(minutes=45)
        context = { 'req':req,'start':start,'time':time,'start_time':start_time, 'end_time':end_time,'email':email,'form':form}
        return  render(request, 'vendor.html', context)
    return render(request,'vendor.html',{'form':form})
        

    



def booking(request):
    if request.method =='POST':
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    form=BookingForm()
    dict_form={
        'form':form
    }
    return render(request, 'booking.html', dict_form)

def contact(request):
    if request.method== 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name =form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            html = render_to_string('contact.html',{
                'name': name,
                'email': email,
                'phone': phone,
                'subject': subject,
                'message': message
            })
            send_mail('The contact form subject', 'This is the message', 'noreply@hotmail.com', ['simacoder@hotmail.com'], html_message=html)
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def searchbar(request):
    if request.method=="POST":
        searched = request.POST['searched']
        event = Event.objects.filter(name__contains=searched)
        return render(request, 'searchbar.html', {'searched': searched, 'events': event})
    else:
        return render(request, 'searchbar.html')


def success(request):
    return HttpResponse('Success!')




def search_locations(request):
    client = square.Client(access_token='EAAAln6qiXnwtnZ986NdgY0V898ZfCABfl3GDC6gdMwUI-Lrtd8rx0lstjoVnz6s')
    location_api = client.locations
    search_results = location_api.search_locations(
        query=request.GET.get('query'),
        location_types=['ADDRESS']
    )
    return render(request, 'base.html', {'search_results': search_results})

def base(request):
	if request.method == "POST":
		searched = request.POST['searched']
		events = Event.objects.filter(description__contains=searched)
	
		return render(request, 
		'base.html', 
		{'searched':searched,
		'events':events})
	else:
		return render(request, 
		'base.html', 
		{})


def process_payment(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        if amount:
            payment = Payment.objects.create(amount=amount)
            return JsonResponse({'success': True, 'message': 'Payment processed successfully'})
    return JsonResponse({'success': False, 'message': 'Payment failed'})

