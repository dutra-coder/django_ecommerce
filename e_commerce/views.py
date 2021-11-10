from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm
def home_page(request) :
    context = {
        "title": "Main Page",
        "content": "Welcome to Main page"
    }
    return render(request, "home_page.html",context)

def about_page(request) :
    context = {
        "title": "About Page",
        "content": "Welcome to About page"
    }
    return render(request, "about/view.html",context)
    
def contact_page(request) :
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page",
        "content": "Welcome to Contact page",
        "form": contact_form
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('name'))
    #     print(request.POST.get('email'))
    #     print(request.POST.get('message'))
    return render(request, "contact/view.html",context)