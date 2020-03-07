from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name='data'
urlpatterns = [
    
    path('',views.list,name="good"),
    path('create/',views.create_data,name="create"),
    re_path('(?P<slug>[\w-]+)/$',views.article,name="detail"),
]
