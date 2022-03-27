from unicodedata import name
from . import viewes
from django.urls import path

urlpatterns = [
    path('', viewes.sec_app_home, name='data_home'),
    path('create/', viewes.create, name='create'),
    path('<int:pk>', viewes.DataDetailNew.as_view(), name='news_datail'),
    path('<int:pk>/update', viewes.DataUpdateNew.as_view(), name='news_update'),
    path('<int:pk>/delete', viewes.DataDeleteNew.as_view(), name='news_delete'),
]
