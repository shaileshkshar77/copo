from django.shortcuts import render
from django.http import HttpResponse
from .models import Copo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
def homepage(request):
    return HttpResponse("Homepage2")

from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout

# Create your views here.

def signup_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            #log
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('accounts:good')
    else:
        form=UserCreationForm()
    return render(request,'accounts/signup.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            #login
            user=form.get_user()
            login(request,user)
            return redirect('accounts:good')
    else:
        form=AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('accounts:good')

def list(request):
    articles=Copo.objects.all()
    return render(request ,"accounts/list.html",{"articles":articles})
    
def article(request,slug):
    #return HttpResponse(slug)
    song=Copo.objects.get(slug=slug)
    return render(request ,"accounts/datas.html",{"song":song})

@login_required(login_url="/accounts/login/")
def create_data(request):
    if request.method =='POST':
        form=forms.Createdata(request.POST,request.FILES)
        if form.is_valid():
            #save database
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('accounts:good')
    else:
        form =forms.Createdata()
    return render(request,"accounts/create.html",{'form':form})

