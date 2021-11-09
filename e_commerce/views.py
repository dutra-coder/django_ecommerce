from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request, "about_page.html",context)
    
def contact_page(request) :
    context = {
        "title": "Contact Page",
        "content": "Welcome to Contact page"
    }
    return render(request, "contact_page.html",context)