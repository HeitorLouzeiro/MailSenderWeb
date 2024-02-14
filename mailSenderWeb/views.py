from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render


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

        # Return a success message
        return HttpResponse(email + ' ' + subject + ' ' + message)
    return render(request, template_name)
