from django.contrib import admin
from django.urls import path
from . import views
app_name = 'exchange'

urlpatterns = [
    path('create/', views.create, name='create'),

    path('details/<int:pk>//', views.details, name='details'),

    path('index/', views.index, name='index'),

    path('my_exch/', views.my_exch, name='my_exch'),


]
