from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import User, Movie, Genre
from .form import LoginForm, SignupForm

import requests

def home(request):
    movie_qs = Movie.objects.all()
    #print (movie_qs)
    if request.session.has_key('email'):
        session = request.session['email']
        return render(request, 'home.html', {"movies": movie_qs, "session": session})
        
    else:
        return render(request, 'home.html', {"movies": movie_qs})

def signup(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid() and (request.POST.get("password") == request.POST.get("confirm_password")):
            data = User(name=request.POST.get("name"), email=request.POST.get("email"), password=request.POST.get("password"), confirm_password=request.POST.get("confirm_password"))
            data.save()
            # redirect to a new URL:
            return redirect('login')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form':form})

def login(request):
     # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if User.objects.filter(email=request.POST.get("email"), password=request.POST.get("password")):
            request.session['email'] = request.POST.get("email")
            print (request.session['email'])
            print (request.user)
            return redirect('home')
        else:
            return HttpResponse('<p style="color:red; text-align:center; font-size:xx-large; font-weight:bolder;">\
                Wrong email or password!!</p>')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
        return redirect('home')
    else:
        return HttpResponse("<strong>Something went wrong</strong>")


def search(request):
    if request.method == 'POST':
        movie_title = request.POST['search']
        response = requests.get(f"http://www.omdbapi.com/?t={movie_title}&apikey=198361c3")
        output_response = response.json()
        #print (output_response)
        print(movie_title)
        if request.session.has_key('email'):
            session = request.session['email']
            return render(request, 'home.html', {'response': output_response, "session": session})
        else:   
            return render(request, 'home.html', { 'response': output_response })

    else:
        return redirect('home')