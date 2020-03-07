from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render,redirect
from data.models import Copo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from data import forms

app_name='hey'

def homepage(request):
    return HttpResponse("Homepage")

