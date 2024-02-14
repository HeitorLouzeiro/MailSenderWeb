import os

from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import HttpResponse, redirect, render
from validate_email import validate_email


# Create your views here.
def home(request):
    template_name = 'index.html'
    if request.method == 'POST':
        # Get the data from the form
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        file = request.FILES.get('file')
        message = request.POST.get('message')

        if email == '' or subject == '' or message == '':
            messages.info(
                request, 'Please fill in email, subject and message fields')
            return render(request, template_name)

        if not validate_email(email):
            messages.info(request, 'Invalid email address')
            return render(request, template_name)

        # Return a success message
            # Crie o objeto EmailMessage
        email_message = EmailMessage(
            subject=subject,
            body=message + '\n\nSent by: ' + email,
            from_email='',
            to=[os.environ.get('EMAIL_HOST_USER')],
        )
        # Anexe o arquivo ao email
        if file:
            email_message.attach(file.name, file.read(), file.content_type)
        # Envie o email
        email_message.send()

        messages.success(request, 'Email sent successfully')
        return redirect('home')

    return render(request, template_name)
