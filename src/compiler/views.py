from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseForbidden, HttpResponse, HttpResponseBadRequest

import requests
import json

from .models import Code
from .utils import isPermittedLang, emptySource

# API Endpoints for hackerearth 
RUN_URL = 'https://api.hackerearth.com/v3/code/run/'
COMPILE_URL = 'https://api.hackerearth.com/v3/code/'

CLIENT_SECRET = settings.CLIENT_SECRET

def index(request):
    context = {
        "title": "Code Pro",
    }
    return render(request, 'index.html', context)

def compileCode(request):
    if request.is_ajax():
        source = request.POST.get('source')
        lang = request.POST.get('lang')        
        isPermittedLang(lang)
        emptySource(source)

        data = {
            "client_secret": CLIENT_SECRET,
            "async": 1,
            "source": source,
            "lang": lang,
        }
        res = requests.post(COMPILE_URL, data=data)
        return JsonResponse(res.json(), safe=True)        
    return HttpResponseBadRequest()

def runCode(request):
    if request.is_ajax():
        source = request.POST.get('source')
        lang = request.POST.get('lang')        
        isPermittedLang(lang)
        emptySource(source)
        
        time_limit = request.POST.get('time_limit', 5) # Default time limit from the HAckerearth docs
        memory_limit = request.POST.get('memory_limit', 262144) # Default memory limit from the HAckerearth docs

        data = {
            "client_secret": CLIENT_SECRET,
            "async": 1,
            "source": source,
            "lang": lang,
            'time_limit': time_limit,
            'memory_limit': memory_limit,
        }
        if 'input' in request.POST:
            data['input'] = request.POST.get('input')
            code_input = request.POST.get('input')

        res = requests.post(RUN_URL, data=data)
        saveCode(res.json(), source, lang, code_input)
        return JsonResponse(res.json(), safe=True)        
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






# compile_data = {
#     'clientId': 'e09c28f7f3a028713f781da2ba32915a',
#     'clientSecret': '388ef2e8baa99a6c27098ca90f7e57a4c441759436fcea5b211313e10ee2bd53',        
#     'script': "print ('Hello World')",
#     'language': "python3",
#     "versionIndex": "0",
# }
# headers = {
#     "Content-Type": "application/json"
# }
# r = requests.post('https://api.jdoodle.com/v1/execute', data=json.dumps(compile_data), headers=headers)
# print(r.json())