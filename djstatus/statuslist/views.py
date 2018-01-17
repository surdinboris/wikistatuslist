from django.shortcuts import render

from django.shortcuts import HttpResponse,HttpResponseRedirect


def home(request):
    return HttpResponseRedirect('ya.ru')
# Create your views here.
