from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import ArcticlesForm
from .models import Arcticles
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.models import User, Group


class DataDetailNew(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'second_app.view_arcticles'
    model = Arcticles
    template_name = 'second_app/details_view.html'
    context_object_name = 'arcticle'


class DataUpdateNew(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'second_app.change_arcticles'
    model = Arcticles
    template_name = 'second_app/create.html'
    form_class = ArcticlesForm


class DataDeleteNew(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'second_app.delete_arcticles'
    model = Arcticles
    success_url = '/data'
    template_name = 'second_app/delete_news.html'
    form_class = ArcticlesForm


def sec_app_home(request):
    news = Arcticles.objects.all().order_by('-date')
    return render(request, 'second_app/home.html', {'news': news})


@login_required(login_url='/accounts/login/')
@permission_required('second_app.add_arcticles')
def create(request):
    print('request.method = ', request.method)
    if request.method == 'POST':
        form = ArcticlesForm(request.POST)
        print('form is valid = ', form.is_valid())
        if form.is_valid():
            form.save()
            return redirect('data_home')

    form = ArcticlesForm()
    data = {
        'form': form
    }
    return render(request, 'second_app/create.html', data)
