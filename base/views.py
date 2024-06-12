from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Save the contact information to the database
        contact = Contact(name=name, email=email, subject=subject, message=message, date=datetime.today())
        contact.save()

        # Display success message
        messages.success(request, 'Your message has been sent successfully!')
        
        # Redirect to home page after form submission
        return redirect('home')

    # If the request method is not POST, just render the home page
    return redirect('home')
