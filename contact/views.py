from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage


def contact(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        # Create a new form instance and fill its fields with the user information
        # that is a query dictionary in request.POST, we do that for check if the form is valid
        form_with_data = ContactForm(data=request.POST)
        # validate if the form data full filed by the user is valid
        if form_with_data.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Send email
            new_email = EmailMessage(
                'La caffetiera: Nuevo mensaje de contacto',
                f'De {name} <{email}>\n\nEscribio:\n\n{content}',
                'no-contestar@inbox.mailtrap.io',
                ['frakodev@devs.com'],
                reply_to=[email]
            )

            try:
                new_email.send()
                # if everything is ok we redirect to the same page but send
                # a string "ok" for inform to user that the form was successfuly sent
                return redirect(reverse('contact') + "?ok")
                # ?ok must be in double quoutes "" if you use simple quotes '' it will fail
            except Exception as e:
                # if something is wrong we redirect to the same page but send
                # a string "fail" for inform to user that the form was not successfuly sent
                return redirect(reverse('contact') + "?fail")

    return render(request, 'contact/contact.html', {'form': contact_form})
