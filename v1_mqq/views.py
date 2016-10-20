from django.http import HttpResponse
from django.http import HttpRequest
#from django.shortcuts import render
import os
import json

from v1_mqq.models import Mqq

def home(request):
    text = """<h1>MQQ</h1>"""
    if request.method == "GET":
        text = text + "Méthode GET"
    elif request.method == "POST" or request.method == "DELETE" or request.method == "PATCH":
        json_content = request.body
        json_content = json_content.decode('utf-8')
        dic = json.loads(json_content)
        a = dic['alias']
        t = dic['type'] 
        e = dic['env'] 
        d = dic['deep']
        if request.method == "POST":
            mqq = Mqq(alias=a, env=e, type=t, deep=d)
            mqq.save()
            HttpResponse.status_code = '200'
        elif request.method == "DELETE":
            mqq = Mqq.objects.get(alias=a, env=e)
            mqq.delete()
            HttpResponse.status_code = '200'
        elif request.method == "PATCH":
            mqq = Mqq.objects.get(alias=a, env=e)
            mqq.type = t
            mqq.deep = d
            mqq.save()
            HttpResponse.status_code = '200'
        else:
            HttpResponse.status_code = '501'
            #I don't even think being here

    return HttpResponse(text)