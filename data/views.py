from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Marks
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def list(request):
    articles=Marks.objects.all()
    return render(request ,"data/list.html",{"articles":articles})


@login_required(login_url="/accounts/login/")
def marks(request):
    if request.method =='POST':
        form=forms.Marks_form(request.POST,request.FILES)
        if form.is_valid():
            #save database
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('data:good')
    else:
        form =forms.Marks_form()
    return render(request,"data/create.html",{'form':form})

@login_required(login_url="/accounts/login/")
def course(request):
    if request.method =='POST':
        form=forms.Marks_Courses(request.POST,request.FILES)
        if form.is_valid():
            #save database
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('data:good')
    else:
        form =forms.Marks_Courses()
    return render(request,"data/courses.html",{'form':form})
@login_required(login_url="/accounts/login/")
def student(request):
    if request.method =='POST':
        form=forms.Marks_Info(request.POST,request.FILES)
        if form.is_valid():
            #save database
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('data:good')
    else:
        form =forms.Marks_Info()
    return render(request,"data/info.html",{'form':form})