# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.contrib import messages

from .models import *

def index(request):
    return render(request, 'login_register/index.html')

def welcome(request):
    context={
        'users':User.objects.get(username=request.session['user']),
        'tables':User.objects.all(),
    }
    return render(request, 'login_register/welcome.html', context)

def register(request):
    errors = User.objects.rvalidator(request.POST)
    if len(errors):
        for error in errors:
            messages.error(request, error)
        return redirect ('/')
    else:
        name=request.POST['name']
        username=request.POST['username']
        password=request.POST['password']
        User.objects.create(name=name, username=username, password=password)
        request.session['user']=username
        return redirect('/welcome')
        

def login(request):
    lerrors = User.objects.lvalidator(request.POST)
    if len(lerrors):
        for lerror in lerrors:
            messages.error(request, lerror)
        return redirect('/')
    else:
        name=request.POST['lname']
        request.session['user']=name
        return redirect('/welcome')
def logout(request):
    return redirect('/')

def poke(request, id):
    poker=User.objects.get(username=request.session['user'])
    pokee=User.objects.get(id=id)
    Poker.objects.create(poker=poker, pokee=pokee)
    return redirect('/welcome')




# Create your views here.
