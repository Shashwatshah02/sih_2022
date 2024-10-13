from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("importantdates", views.importantdates, name='importantdates'),
    path("downloads", views.downloads, name='downloads'),
    path("faqs", views.faqs, name='faqs'),
    path("contactus", views.contactus, name='contactus'),
]