from django.conf.urls import url 
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
]