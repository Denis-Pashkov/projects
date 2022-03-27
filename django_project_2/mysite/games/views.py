from django.contrib.auth.mixins import LoginRequiredMixin
from pyexpat import model
from attr import fields
from django.shortcuts import render, redirect
# from django.views.generic import ListView
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

@login_required
def games(request):
    return render(request, 'games/games.html')

@login_required
def saper(request):
    return render(request, 'games/saper.html')

@login_required
def calc(request):
    return render(request, 'games/calc.html')
# Create your views here.
