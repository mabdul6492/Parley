from django.shortcuts import render
from .models import Contact
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def contact(request):
    if request.method == 'POST':
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST['message']
        contact.name = name
        contact.email = email
        contact.subject = subject
        contact.message = message
        contact.save()

        return render(request, 'success.html')
    return render(request, 'contact.html')
