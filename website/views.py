from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from website.models import Contact
from website.forms import ContactForm

# Create your views here.
def index(request):
    return render(request, 'website/index.html')


def about(request):
    return render(request, 'website/about.html')


def contact(request):
    contact = ContactForm(request.POST)
    if request.method == 'POST':
        if contact.is_valid():
            contact.save()
            print("for is valid $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        else :
            print("for is not valid $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")


    return render(request, 'website/contact.html', context={'form':contact})


def elements(request):
    return render(request, 'website/elements.html')

def formTest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mail = request.POST.get('mail')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        c = Contact()
        c.name = name
        c.mail = mail
        c.subject = subject
        c.message = message
        c.save()
    else:
        print("request method is GET")
    return render(request, 'website/form.html')


def testView(request):
    if request.method == 'POST':
        contact = ContactForm(request.POST)
        # if contact.is_valid():
        #     name = contact.cleaned_data['name']
        #     email = contact.cleaned_data['email']
        #     subject = contact.cleaned_data['subject']
        #     message = contact.cleaned_data['message']
        #     c = Contact()
        #     c.name = name
        #     c.email = email
        #     c.subject = subject
        #     c.message = message
        #     c.save()
        if contact.is_valid():
            contact.save()
            return HttpResponse("Done")
        else:
            return HttpResponse("form input parameters are not valid")
    else:
        
        form = ContactForm()
    return render(request, 'website/form.html', {'form': form})