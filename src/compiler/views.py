from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

import requests
import json

from .models import Code
from .utils import isPermittedLang, emptySource

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
    

def saveCode(res, source, lang, input):
    code_id = res['code_id']
    compile_status = res['compile_status']
    run_status = res['run_status']['status']
    run_time = res['run_status']['time_used']
    run_mem = res['run_status']['memory_used']
    op_html = res['run_status']['output_html']

    new_code = Code.objects.create(
        id = code_id,
        content = source,
        language = lang,
        input = input,
        compile_status = compile_status,
        run_status = run_status,
        run_time = run_time,
        run_memory = run_mem,
        output_html = op_html
    )
    new_code.save()


def viewSavedCode(request, code_id=None):
    result = codes.objects.get(id=code_id).first()
    result = result.to_json()
    result = json.loads(result)

    content = result['content']
    lang = result['language']
    input = result['input']
    compile_status = result['compile_status']
    run_status = result['run_status']
    run_time = result['run_time']
    run_memory = result['run_memory']
    run_output = result['run_output']

    context = {
        'content': content,
        'lang': lang,
        'inp': input,
        'compile_status': compile_status,
        'run_status': run_status,
        'run_time': run_time,
        'run_output': run_output,
        'run_memory': run_memory,
    }

    return render(request, 'index.html', context)