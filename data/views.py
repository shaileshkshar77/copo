from django.shortcuts import render,redirect
from .models import Copo
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def list(request):
    articles=Copo.objects.all()
    return render(request ,"data/list.html",{"articles":articles})
    
def article(request,slug):
    #return HttpResponse(slug)
    song=Copo.objects.get(slug=slug)
    return render(request ,"data/datas.html",{"song":song})

@login_required(login_url="/accounts/login/")
def create_data(request):
    if request.method =='POST':
        form=forms.Createdata(request.POST,request.FILES)
        if form.is_valid():
            #save database
            inst=form.save(commit=False)
            inst.author=request.user
            inst.save()
            return redirect('data:good')
    else:
        form =forms.Createdata()
    return render(request,"data/create.html",{'form':form})
