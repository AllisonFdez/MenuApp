# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http 	  import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
from menu.forms import SigninForm


# Create your views here.

def index(request):
	return render(request, 'index.html',{})

def menu(request):
	return render(request, 'menu.html',{})

def login(request):
	return render(request, 'login.html',{})

def signin(request):
	if request.method =="POST":
		form = SigninForm(request.POST)
		if form.is_valid():
		   form.save()
		   return redirect('/menu')
	else:
		form = SigninForm()

	return render(request,'signin.html',{'form': form})
		
