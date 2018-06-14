from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

import requests
import json

from authenticate.models import User
from .models import Code
from .utils import isPermittedLang, emptySource, create_unique_id, id_generator

# API Endpoint for hackerearth 
RUN_URL = 'https://api.hackerearth.com/v3/code/run/'

CLIENT_SECRET = settings.CLIENT_SECRET

def index(request):
    context = {
        "title": "Code Pro",
    }
    return render(request, 'index.html', context)

def executeCode(request):
    if request.is_ajax():
        # source = "print 'Hello World'"
        source = request.POST.get('source')
        lang = request.POST.get('lang')
        data = {
            'client_secret': CLIENT_SECRET,
            'async': 0,
            'source': source,
            'lang': lang,
            'time_limit': 5,
            'memory_limit': 262144,
        }
        if 'input' in request.POST:
            data['input'] = request.POST.get('input')

        res = requests.post(RUN_URL, data=data)
        print(res.json())
        return JsonResponse(res.json(), safe=False)    
    return HttpResponseBadRequest()
    

def saveCode(request):
    if request.is_ajax():
        id = create_unique_id()
        content = request.POST.get('content')
        lang = request.POST.get('lang')
        name = request.POST.get('codeName')
        input = request.POST.get('input')
        owner = request.session['username']

        new_code = Code.objects.create(
            id = id,
            name = name,
            content = content,
            language = lang,
            input = input,
            owner = owner,
        )
        new_code.save()
        res = {}
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()

def profile(request):
    if request.is_ajax():
        username = request.session['username']
        print(username)
        qs = Code.objects.filter(owner__iexact=username)
        code_id = []
        code_name = []
        code_timestamp = []
        for obj in qs:
            code_id.append(obj.id)
            code_name.append(obj.name)
            code_timestamp.append(obj.timestamp)
        print(code_id)
        print(code_name)
        res = {
            'code_id': code_id,
            'code_name': code_name,
            'code_timestamp': code_timestamp,
        }
        return JsonResponse(res, safe=False)
    return HttpResponseBadRequest()


def deleteCode(request):
    if request.is_ajax():
        code_id = request.POST.get('id')
        user = request.session['username']
        obj = Code.objects.filter(id__iexact=code_id).filter(owner__iexact=user).first()
        print(obj)
        obj.delete()
        return JsonResponse({}, safe=False)
    return HttpResponseBadRequest()

def viewSavedCode(request):
    if request.is_ajax():
        code_id = request.POST.get('id')
        obj = Code.objects.filter(id__iexact=code_id).first()
        content = obj.content
        title = obj.name
        res = {
            'content': content,
            'title': title,
        }
        return JsonResponse(res, safe=False)
    return HttpResponseBadRequest()