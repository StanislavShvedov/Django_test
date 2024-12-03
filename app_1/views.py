import datetime
import os

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.urls import reverse


# Create your views here.

def home_view(request: HttpRequest):
    template_name = 'home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request: HttpRequest):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')


def workdir_view(request: HttpRequest):
    work_dir = os.listdir(os.getcwd())
    return HttpResponse(f'Содержимое рабочей директории: {', '.join(work_dir)}')
