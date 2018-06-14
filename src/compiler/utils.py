from django.http import JsonResponse

import string
import random

from .models import Code

PERMITTED_LANG = ["C", "CPP", "CSHARP", "CLOJURE", "CSS", "HASKELL", "JAVA", "JAVASCRIPT", "OBJECTIVEC", "PERL", "PHP", "PYTHON", "R", "RUBY", "RUST", "SCALA"]

def isPermittedLang(lang):
    if lang.upper not in PERMITTED_LANG:
        response = {
            "message": "ERROR: Invalid language",
        }
        return JsonResponse(response, safe=False)

def emptySource(source):
    if ((source == "") or (len(source) == 0)):
        response = {
            "message": "ERROR: Empty Source",
        }
        return JsonResponse(response, safe=False)


def id_generator():
    size = 6
    chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def create_unique_id():
    new_id = id_generator()
    qs_exists = Code.objects.filter(id=new_id).exists()
    if qs_exists:
        return create_unique_id()
    return new_id