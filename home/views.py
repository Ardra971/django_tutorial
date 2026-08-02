from django.shortcuts import render, redirect  
from django.http import HttpResponse
from django.contrib import messages
from .models import departments as DepartmentModel
from .models import Doctors as DoctorsModel
from .models import ContactMessage

from .forms import BookingForm

def index(request):
    person = {
        'name': 'John Doe',
        'age': 30,
        'city': 'New York'
    }
    return render(request, 'index.html', person)

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def doctors(request):
    dict_docs = {
        'doctors': DoctorsModel.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)

def contact(request):
    if request.method == 'POST':
        # Extract inputs from the HTML form fields using their 'name' attributes
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Instantiate and save into database
        new_msg = ContactMessage(name=name, email=email, subject=subject, message=message)
        new_msg.save()

        # Display a green success notification popup
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')

    return render(request, 'contact.html')

def departments(request):
    dic_dept = {
        'dept': DepartmentModel.objects.all()
    }
    return render(request, 'departments.html', dic_dept)