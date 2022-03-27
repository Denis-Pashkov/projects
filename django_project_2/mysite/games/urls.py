from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    path('', views.games, name='games'),
    path('saper', views.saper, name='saper'),
    path('calc', views.calc, name='calc'),
]
