from django.shortcuts import render
import datetime
from django.shortcuts import render, redirect
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login
from .forms import RegisterUserForm


def home_page(request):
    return render(request, 'first_app/home.html', {'bgimage': '../../static/first_app/img/pexels-francesco-ungaro-2325446.jpg'})


def cur_date_time(request):
    date = datetime.datetime.now()
    return render(request, 'first_app/cur_date_time.html', {'date': date, 'bgimage': '../../static/first_app/img/pexels-denise-duplinski-3814319.jpg'})


def contacts_page(request):
    data = {'phone_list': ['89298479174', '89284847583',
                           '89234474623', '89234474621'], 'bgimage': '../../static/first_app/img/pexels-denise-duplinski-3819818.jpg'}
    return render(request, 'first_app/contacts.html', data)
# Create your views here.


class register(CreateView):
    form_class = RegisterUserForm
    template_name = 'first_app/register.html'
    seccess_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
