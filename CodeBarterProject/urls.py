from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('user/', include('user.urls')),

    path('skills/', include('skills.urls')),

    path('exchange/', include('exchange.urls')),

    path('accounts/', include('django.contrib.auth.urls')),

]
