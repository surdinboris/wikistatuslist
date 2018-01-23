from django.shortcuts import render,reverse
from django.shortcuts import HttpResponse,HttpResponseRedirect,redirect
from tagparser import *
import os
import re
import graphos

def main(request):

    return HttpResponse('Statuslist')
# Create your views here.

def detail(request,ibox):
    ct="system not found"
    lst=[f for f in os.listdir(os.path.join(os.getcwd(), 'cdc/'))]
    for lso in lst:
        sr=re.search(r'({})'.format(ibox),lso.replace(".txt",""))
        if sr:
            print('request found in wikipages')
            parsr = Collector(os.path.join(os.getcwd(), 'cdc/', lso))
            ct=parsr.tagsclctr
            print(ct)
            # print(ct)
            # ct=[item for item in parsr.tagsclctr.values()]
            #ct=[' '.join([str(key), ' '.join(item)]) for key, item in parsr.tagsclctr.items()]


            # for key, item in parsr.tagsclctr.items():
            #     d=' '.join([str(key), ' '.join(item)]) #joining contents of dict
            #     print(d)

            #implementing of calculation algorythom
            #implementing of http://www.dangtrinh.com/2013/07/django-celery-display-progress-bar-of.html
            #use database for sroring progress info that periodically will be updated from task lists
            #finishing with closing status and remooving of finished
            #
    print(type(ct))

    return render(request,'detail.html', {'ibox': ibox, 'ct':ct})