from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')),
    path('captcha/', include('captcha.urls')),
]