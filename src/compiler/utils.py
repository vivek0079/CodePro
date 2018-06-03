from django.http import JsonResponse

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