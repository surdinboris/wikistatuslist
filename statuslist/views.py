from django.shortcuts import render

from django.shortcuts import HttpResponse,HttpResponseRedirect,redirect


def home(request):
    return redirect("http://stackoverflow.com/")
# Create your views here.
