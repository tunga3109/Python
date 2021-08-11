from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h4>Проверка работает</h4>")

def about(request):
    return HttpResponse("<h4>Страница про нас</h4>")

def you(request):
    return HttpResponse("<h4>Долбоеб</h4>")
    
    
