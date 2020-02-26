from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [

    path('signup/',views.signup_view,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('',views.homepage),
]
