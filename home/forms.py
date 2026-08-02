from django import forms
from .models import bookings
class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = bookings
        fields = '__all__'
        widgets = {
            'booking_date': DateInput()
        }

        labels = {
            'p_name': 'Patient Name',
            'p_phone': 'Patient Phone',
            'p_email': 'Patient Email',
            'doc_name': 'Doctor',
            'booking_date': 'Booking Date'
        }