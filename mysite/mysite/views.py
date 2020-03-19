from django.http import HttpResponse
from django.shortcuts import render


def index_view(request):
    return render(request, 'base.html')


def sport_view(request):
    return  render(request,'sports.html')


def news_view(request):
    pass
