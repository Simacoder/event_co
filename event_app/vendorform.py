from django import forms

class DateInput(forms.DateInput):
    input_type='date'



class BookingFormv(forms.Form):
    eventTitle = forms.CharField(label="event", max_length=255, required=True)
    startDateTime = forms.DateTimeField(label="startDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)
    endDateTime = forms.DateTimeField(label="endDateTime", input_formats=['%Y/%m/%d %H:%M'], required=True)