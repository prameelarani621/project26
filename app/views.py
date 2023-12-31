from django.shortcuts import render
from app.models import *

from django.http import HttpResponse
# Create your views here.
def insert_topic(request):

    if request.method=='POST':
        tn=request.POST['tn']

        TO=Topic.objects.get_or_create(topic_name=tn)[0]

        TO.save()

        QLTO=Topic.objects.all()
        d={'topics':QLTO}
        return render(request,'display_topic.html',d)


    return render(request,'insert_topic.html')


def insert_WebPages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}
    if request.method=='POST':
        tn=request.POST['tn']
        na=request.POST['na']
        ur=request.POST['ur']
        em=request.POST['em']
        TO=Topic.objects.get(topic_name=tn)
        WO=WebPage.objects.get_or_create(topic_name=TO,name=na,url=ur,email=em)[0]
        WO.save()
        QLWO=WebPage.objects.all()
        d1={'WebPages':QLWO}
        return render(request,'display_WebPages.html',d1)

    return render(request,'insert_WebPages.html',d)


def multipul_records_webpages(request):
    QLTO=Topic.objects.all()
    d={'topics':QLTO}

    if request.method=='POST':
        topiclist=request.POST.getlist('tn')#['C','FB','VB']
        #print(tn)
        QLWO=WebPage.objects.none()
        for i in topiclist:
            QLWO=QLWO|WebPage.objects.filter(topic_name=i)

        d1={'WebPages':QLWO}
        return render(request,'display_WebPages.html',d1) 

    return render(request,'multipul_records_webpages.html',d)
