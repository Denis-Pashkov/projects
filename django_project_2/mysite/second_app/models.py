from statistics import mode
from tabnanny import verbose
from turtle import title
from django.db import models
from django.shortcuts import redirect


class Arcticles(models.Model):
    title = models.CharField('Название', max_length=50, default='')
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return(self.title)
    
    def get_absolute_url(self):
        return f'/data/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
# Create your models here.
