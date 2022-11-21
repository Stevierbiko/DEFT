from django.conf import settings
from django.shortcuts import render,redirect


# Create your views here.

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request, 'products.html')


def contact(request):
    # if request.method == 'POST':
    #     form = ContactForm(request.POST)

    #     if form.is_valid():
    #         full_name = form.cleaned_data['full_name']
    #         company_name = form.cleaned_data['company_name']
    #         email = form.cleaned_data['email']
    #         message = form.cleaned_data['message']

    #         html = render_to_string('emails/contactform.html', {
    #             'full_name ': full_name ,
    #             'company_name': company_name,
    #             'email': email,
    #             'message': message
    #         })

    #         send_mail('The contact form subject', 'This is the message', 'noreply@codewithstein.com', ['info@defttech.co.ke'], html_message=html)

    #         return redirect('home')
    # else:
    #     form = ContactForm()

    return render(request, 'contact.html')