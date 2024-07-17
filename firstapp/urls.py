from django.urls import path

from . import views

urlpatterns = [
    path('',views.main,name='home'),
    path('members/',views.members,name='members'),
    path('members/details/<slug:slug>', views.details, name='details'),

]

