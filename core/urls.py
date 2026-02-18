from django.contrib import admin
from django.urls import path
from . import views
app_name='core'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.base, name='base'),
    path('', views.home, name='home'),
    path('features/', views.features, name='features'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),

]
