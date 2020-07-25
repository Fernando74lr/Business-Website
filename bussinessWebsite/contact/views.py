from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

# Create your views here.
def contact(request):
    # Create an empty template.
    contact_form = ContactForm()

    # Check if any data were sent with POST method.
    if request.method == 'POST':
        # If so, we fill up the template with the info.
        contact_form = ContactForm(data=request.POST)

        # Validate form.
        if contact_form.is_valid():
            # As it is a dictionary we can use the accessor get () 
            # to get the field with the key and if there is none that returns an empty string
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            # We send the email and redirect.
            email = EmailMessage(
                "La Caffettiera: New contact message", # Subject
                'From {} <{}>\n\nWrote:\n\n{}'.format(name, email, content), # Body
                'do-not-reply@inbox.mailtrap.io', # Email origin
                ['lopezramirez330@gmail.com'], # Email destiny
                reply_to=[email]
            )
            try:
                email.send()
                return redirect(reverse('contact') + '?ok')
            except:
                # Something went wrong, redirect to fail.
                return redirect(reverse('contact') + '?fail')
            
    return render(request, 'contact/contact.html', {'form': contact_form})