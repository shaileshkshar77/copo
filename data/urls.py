from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name='data'
urlpatterns = [
    path('',views.list,name="good"),
    path('getmarks/',views.marks,name="create"),
    path('students/',views.student,name="students"),
    path('courses/',views.course,name="courses"),
]
