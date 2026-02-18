from django.contrib import admin
from django.urls import path
from . import views
app_name = 'user'
urlpatterns = [
    path('admin/', admin.site.urls),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),
    path('settings/', views.settings, name='settings'),
    path('', views.index, name='index'),

]
