from django.shortcuts import render
from django.http import HttpResponse


app_name='hey'

def homepage(request):
    return HttpResponse("Homepage")

