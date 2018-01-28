from django.shortcuts import render,reverse
from django.shortcuts import HttpResponse,HttpResponseRedirect,redirect
from tagparser import *
import os
import re
import json

def main(request):
    wikiplist=[f for f in os.listdir(os.path.join(os.getcwd(), 'cdc/'))]
    wikistat={}
    for wikip in wikiplist: #parsing each wikipage and counting missions that were done
        wikipname=wikip.replace(".txt","").upper()
        tagstat={}
        tagstat['stations'] = {}
        parsr = Collector(os.path.join(os.getcwd(), 'cdc/', wikip))
        tags=(parsr.tagsclctr).values()
        done = 0
        for tag in tags:
            #tagstat['stations'].update({tag['station']: {}})
            if not tag['station'] in tagstat['stations']: #initialising tag station if not exist
                tagstat['stations'].update({tag['station']: {'Done':0,'Pending':0,'Total':0}})
            if tag['status']  == 'Done':
                ((tagstat['stations'])[tag['station']])['Done'] += 1
                ((tagstat['stations'])[tag['station']])['Total'] += 1
                done += 1 #main counter update
            elif tag['status']  == 'Pending':
                 ((tagstat['stations'])[tag['station']])['Pending'] += 1
                 ((tagstat['stations'])[tag['station']])['Total'] += 1

        tagstat['wikipname']=wikipname
        tagstat['total']=len(tags)
        tagstat['done']=done
        tagstat['perc']=done/(len(tags))*100
        wikistat[wikipname]=tagstat

    return render(request,'status.html', {'wikistat': json.dumps(wikistat)})

def detail(request,ibox):
    tags={}
    wikiplist=[f for f in os.listdir(os.path.join(os.getcwd(), 'cdc/'))]
    for wikip in wikiplist: #searching for apropriate page with request
        wikipname=re.search(r'({})'.format(ibox.lower()),wikip.replace(".txt",""))
        if wikipname:
            parsr = Collector(os.path.join(os.getcwd(), 'cdc/', wikip))
            tags=parsr.tagsclctr
    return render(request,'detail.html', {'ibox': ibox, 'tags':tags})