from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(request):
    return HttpResponse("Homepage2")

def signup_view(request):
    return HttpResponse("Signup")
    
def login_view(request):
    return HttpResponse("login")
    

def logout_view(request):
    return HttpResponse("logout")
    
