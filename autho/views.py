from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect 
from .forms import RegisterForm
from django.contrib.auth.forms import AuthenticationForm #authenticationform er moddhe username and password ta thake arki
from django.contrib.auth import *
from bookmanagement.models import *
from django.contrib.auth.models import User
from django.contrib import messages







# Create your views here.

def home (request):
    return render(request, 'autho/text.html', {
        'warning': "You Seem Lost Kid. What Are You Doing Here?"
    })
    


def signout(request):
    logout(request)
    return render(request, 'autho/text.html', {
        'warning': "Logged Out Successfully"
    })


def signup (request):
    
    if request.method == 'POST':
        logout(request) #handled
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save() #form.save dile data gulo backend e chole jabe. however, apatoto commit korchi na so save(commit=False)...
            messages.success(request, "Account Created Successfully")
            #print(form.cleaned_data) # to print in console
            #
            return render(request, 'autho/text.html', {
        'warning': "Account Created Successfully"})
    else:
        form = RegisterForm()
        return render(request, "autho/signup.html", {'form' : form })
    
    return render(request, "autho/signup.html", {'form' : form })
    

    


def signin (request):
    if request.method == 'POST':
        
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            un = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            user = authenticate( username=un, password=pw)
            
            
            b = user.borrowedbyRelated.all()
            w = user.wishlistRelated.all()
            
            
            if user:
                login(request, user)
                return render (request, 'autho/profile.html' , {
                    'username': un,
                    'books' : b, 
                    'wish' : w
                }) 
            else:
                return render(request, 'autho/text.html', {
        'warning': "Not Matched"
    })
        else:
           return render(request, 'autho/text.html', {
        'warning': "Not Valid Data"
    })

                
    else: #get request
        if not request.user.is_authenticated:
            form = AuthenticationForm()
            return render(request, "autho/signin.html", {'form' : form })
        else:
            u = request.user
            b = u.borrowedbyRelated.all()
            w = u.wishlistRelated.all()
            return render (request, 'autho/profile.html' , {
                    'username': request.user.username,
                    'books' : b,
                    'wish' : w
                    
                }) 
            


