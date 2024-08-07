from django.shortcuts import render

# Create your views here.

from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}

    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topicname']
            TO=Topic.objects.get_or_create(topicname=tn)[0]
            TO.save()
            return HttpResponse('topic is created')
        else:
            return HttpResponse('invalid topic')

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}

    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topicname']
            na=WFDO.cleaned_data['name']
            url=WFDO.cleaned_data['url']

            TO=Topic.objects.get(topicname=tn)
            WO=Webpage.objects.get_or_create(topicname=TO,name=na,url=url)[0]
            WO.save()
            return HttpResponse('webpage is created')
        else:
            return HttpResponse('invalid data')
        

    return render(request,'insert_webpage.html',d)


def insert_accessrecord(request):
    EAFO=Accessrecordform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=Accessrecordform(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            au=AFDO.cleaned_data['author']
            da=AFDO.cleaned_data['date']
            WO=Webpage.objects.get(name=na)
            AO=Accessrecord.objects.get_or_create(name=WO,author=au,date=da)[0]
            AO.save()
            return HttpResponse('accessrecord is created')
        else:
            return HttpResponse('invalid')

    return render(request,'insert_accessrecord.html',d)
 
