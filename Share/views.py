from django.shortcuts import render
from django.views.generic import View
from .models import Upload
from django.http import HttpResponsePermanentRedirect,HttpResponse
import random
import string
import json
from static.fliter.dogpred import Recognition
import datetime


class HomeView(View):
    def get(self,request):
        return render(request,"base.html",{})

    def post(self,request):
        if request.FILES:
            file = request.FILES.get("file")
            name = file.name
            size = int(file.size)
            with open('static/file/'+name,'wb')as f :
                f.write(file.read())
            code = ''.join(random.sample(string.digits, 8))
            u = Upload(
                path = 'static/file/'+name,
                name=Recognition(name),
                Filesize=size,
                code = code,
                PCIP=str(request.META['REMOTE_ADDR']),
            )
            u.save()

            return HttpResponsePermanentRedirect("/s/"+code)


class DisplayView(View):
    def get(self,request,code):
        u = Upload.objects.filter(code=str(code))
        # u = Upload.objects.all()
        if u :
            for i in u :
                i.DownloadDocount +=1
                i.save()
        return render(request,'content.html',{"content":u})


class MyView(View):
    def get(self,request):
        IP = request.META['REMOTE_ADDR']
        u = Upload.objects.filter(PCIP=str(IP))
        for i in u :
            i.DownloadDocount +=1
            i.save()
        return render(request,'content.html',{"content":u})


class SearchView(View):
    def get(self,request):
        code = request.GET.get("kw")
        u = Upload.objects.filter(name=str(code))
        data = {}
        if u :
            for i in range(len(u)):
                u[i].DownloadDocount +=1
                u[i].save()
                data[i]={}
                data[i]['download'] = u[i].DownloadDocount
                data[i]['filename'] = u[i].name
                data[i]['id'] = u[i].id
                data[i]['ip'] = str(u[i].PCIP)
                data[i]['size'] = u[i].Filesize
                data[i]['time'] = str(u[i].Datatime.strftime('%Y-%m-%d %H:%M:%S'))
                data[i]['key'] = u[i].code

        return HttpResponse(json.dumps(data),content_type="application/json")

class Phone(View):
    def post(self,request):
        if request.FILES:
            file = request.FILES.get("dddd")
            # return HttpResponse(file)
            name = file.name
            size = int(file.size)
            print(name)
            # return HttpResponse("1112")
            with open('static/file/' + name, 'wb')as f:
                f.write(file.read())
            result = Recognition(name)
            code = ''.join(random.sample(string.digits, 8))
            u = Upload(
                path='static/file/' + name,
                name=name,
                Filesize=size,
                code=code,
                PCIP=str(request.META['REMOTE_ADDR']),
                # result=Recognition(),
            )
            u.save()
        print("111111111122")
        return HttpResponse(result)




class ajx(View):
    def get(self,request):
        resp = {'errorcode': 100, 'detail': 'Get success'}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    def post(self,request):


        if request.FILES:
            file = request.FILES.get("files")
            name = file.name
            size = int(file.size)
            with open('static/file/' + name, 'wb')as f:
                f.write(file.read())
            code = ''.join(random.sample(string.digits, 8))
            u = Upload(
                path='static/file/' + name,
                name=Recognition(),
                Filesize=size,
                code=code,
                PCIP=str(request.META['REMOTE_ADDR']),
            )
            u.save()

        # myFile = request.FILES.get("myfile", None)  # 获取上传的文件，如果没有文件，则默认为None
        # name = myFile.name
        # if not myFile:
        #     return HttpResponse("no files for upload!")
        # with open('static/file/' + name, 'wb')as f:
        #     f.write(myFile.read())
        print("111111111122")

        data = {}
        temp = Upload.objects.filter(code=str(code))
        if temp:
            for i in range(len(temp)):
                temp[i].DownloadDocount += 1
                temp[i].save()
                data[i] = {}
                data[i]['download'] = temp[i].DownloadDocount
                data[i]['name'] = temp[i].name
                data[i]['id'] = temp[i].id
                data[i]['ip'] = str(temp[i].PCIP)
                data[i]['size'] = temp[i].Filesize
                data[i]['time'] = str(temp[i].Datatime.strftime('%Y-%m-%d %H:%M:%S'))
                data[i]['key'] = temp[i].code
        return HttpResponse(json.dumps(data), content_type="application/json")
        # Create your views here.
