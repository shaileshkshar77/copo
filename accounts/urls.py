from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import url
from . import views

app_name='accounts'

urlpatterns = [

    path('signup/',views.signup_view,name="signup"),
    path('login/',views.login_view,name="login"),
    path('logout/',views.logout_view,name="logout"),
    path('',views.list,name="good"),
    path('create/',views.create_data,name="create"),
    re_path('(?P<slug>[\w-]+)/$',views.article,name="detail"),
]

