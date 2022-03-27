from django.urls import path, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls, name='admins1'),
    
    # Меню
    path('', views.home_page, name='home'),
    path('ascent/', views.ascent, name='ascent'),
    path('trekking/', views.trekking, name='trekking'),
    path('clients/', views.clients, name='clients'),
    path('contacts/', views.contacts, name='contacts'),
    path('about/', views.about, name='about'),
    
    # Регистрация и вход
    path('accounts/', include('django.contrib.auth.urls')),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('accounts/login/', auth_views.LoginView.as_view()),
    
    # Выпадающее меню
    # Восхождения
    path('ascent/elbrus', views.elbrus, name='elbrus'),
    path('ascent/kilimanjaro', views.kilimanjaro, name='kilimanjaro'),
    path('ascent/lenin_peak', views.lenin_peak, name='lenin_peak'),
    path('ascent/kazbek', views.kazbek, name='kazbek'),
    path('ascent/monblan', views.monblan, name='monblan'),
    path('ascent/peak_separate', views.peak_separate, name='peak_separate'),
    path('ascent/manaslu', views.manaslu, name='manaslu'),
    path('ascent/ararat', views.ararat, name='ararat'),
    path('ascent/aragats', views.aragats, name='aragats'),
    
    # Треккинг
    path('ascent/lician_path', views.lician_path, name='lician_path'),
    path('ascent/arround_annapurna', views.arround_annapurna, name='arround_annapurna'),

    # Клиентам
    path('ascent/clothes_and_equuipment', views.clothes_and_equuipment, name='clothes_and_equuipment'),
    path('ascent/phisical_training', views.phisical_training, name='phisical_training'),
    path('ascent/treaties', views.treaties, name='treaties'),
    path('ascent/question_answer', views.question_answer, name='question_answer'),
    path('ascent/arcticles', views.arcticles, name='arcticles'),

    # О нас
    path('ascent/ourteam', views.ourteam, name='ourteam'),
    path('ascent/photo', views.photo, name='photo'),
    path('ascent/video', views.video, name='video'),
    path('ascent/send_reviews', views.send_reviews, name='send_reviews'),
    path('ascent/reviews', views.reviews.as_view(), name='reviews'),
]
