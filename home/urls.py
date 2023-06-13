from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("home",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact, name='contact'),
    path("kick",views.kick, name='kick'),
    path("poomse",views.poomse, name='poomse'),
    path("fight",views.fight, name='fight'),
    
]