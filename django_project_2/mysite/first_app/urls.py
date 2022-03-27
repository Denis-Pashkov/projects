from . import viewes
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewes.home_page, name='home'),
    path('cur_date_time/', viewes.cur_date_time, name='cur_date_time'),
    path('contacts/', viewes.contacts_page, name='contacts'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('games/', include('games.urls')),
    path('register/', viewes.register.as_view(), name='register')
]
