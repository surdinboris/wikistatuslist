from django.shortcuts import render,reverse
from django.shortcuts import HttpResponse,HttpResponseRedirect,redirect
from tagparser import *
import os
import re


def main(request):
    wikiplist=[f for f in os.listdir(os.path.join(os.getcwd(), 'cdc/'))]
    wikistat={}
    for wikip in wikiplist: #parsing each wikipage and counting missions that were done
        wikipname=wikip.replace(".txt","")
        tagstat={}
        parsr = Collector(os.path.join(os.getcwd(), 'cdc/', wikip))
        tags=(parsr.tagsclctr).values()
        done = 0
        for tag in tags:
            if tag['status']  == 'Done':
                done+=1
        tagstat['wikipname']=wikipname
        tagstat['total']=len(tags)
        tagstat['done']=done
        wikistat[wikipname]=tagstat

    return render(request,'main.html', {'wikistat': wikistat})

def detail(request,ibox):
    tags={}
    wikiplist=[f for f in os.listdir(os.path.join(os.getcwd(), 'cdc/'))]
    for wikip in wikiplist: #searching for apropriate page with request
        wikipname=re.search(r'({})'.format(ibox),wikip.replace(".txt",""))
        if wikipname:
            print('page request found in wikipages %s' %wikipname)
            parsr = Collector(os.path.join(os.getcwd(), 'cdc/', wikip))
            tags=parsr.tagsclctr
    return render(request,'detail.html', {'ibox': ibox, 'tags':tags})