from django.contrib.auth import authenticate, login, get_user_model
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactForm, LoginForm, RegisterForm
def home_page(request) :
    context = {
        "title": "Main Page",
        "content": "Welcome to Main page"
    }
    if request.user.is_authenticated:
        context["premium_content"] = "You are a Premium User"
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

def login_page(request) :
    form = LoginForm(request.POST or None)
    context = {
                    'form':form
              }
    print("User logged in")
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request, username=username, password=password)
        print(user)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            print("Valid login")
            #Redirect to main page
            return redirect("/")
        else:
            #Return an error message "Invalid Login"
            print("Invalid login")
    return render(request, "auth/login.html",context)

User = get_user_model()
def register_page(request) :
    form = RegisterForm(request.POST or None)
    context = {
                    'form':form
              }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        email=form.cleaned_data.get("email")
        password=form.cleaned_data.get("password")
        newuser = User.objects.create_user(username, email, password)
        print(newuser)
    return render(request, "auth/register.html",context)