from django.contrib import admin
from django.urls import path, re_path
from .import views

app_name = 'accounts'

urlpatterns = [
    re_path(r'^signup/$',views.signup,name='signup'),
    re_path(r'^signin/$',views.signin,name='signin'),
    ]
