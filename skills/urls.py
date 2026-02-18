from django.contrib import admin
from django.urls import path
from . import views
app_name='skills'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('myskills', views.myskills, name='myskills'),
    path('', views.index, name='index'),
    path('details/<int:pk>/', views.details, name='details'),
    path('add/', views.add, name='add'),

]
