#!/usr/bin/python3
import os
from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    context={}
    context['hello']='hello ni ma'
    return render(request,'hello.html',context)
    
def index(request):
    return render(request,'index.html','')

def xhr_ajax(request):
    if request.FILES:
       	a=request.FILES['uploadfile'].name
        f = request.FILES.get('uploadfile')
        pwDir = os.path.dirname(os.path.abspath(__name__))
        absDir=os.path.abspath(__name__)
        baseDir=os.path.join(pwDir,'upload') 
        baseDir='/wwwroot/OMMS/upload' 
        filename = os.path.join(baseDir,f.name)
        fout=open(filename,'wb')
        for chrunk in f.chunks():
            fout.write(chrunk.decode('gbk').encode('utf-8'))
        fout.write('\n'.encode('utf-8'))
        fout.close()
        return HttpResponse('The file '+a+' has been saved in '+baseDir+', I am a motherfucking star boy! fuck me!'+'and the absDir is '+absDir)
    else:
        return HttpResponse('Your operation occurs an error')

