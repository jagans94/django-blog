from django.contrib import admin
from django.urls import path, re_path
from .import views

urlpatterns = [
    re_path(r'^$',views.articles,name='list'),
    re_path(r'^(?P<slug>[\w-]+)/$',views.article_details,name='details'),
    ]
