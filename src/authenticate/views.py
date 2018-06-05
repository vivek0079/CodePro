from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse

from passlib.hash import sha256_crypt
import json

from .models import User

def loginUser(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        stayloggedin = request.POST.get('stayloggedin')
        if stayloggedin == "true":
            pass
        else:
            request.session.set_expiry(0)
        status = 0
        user_qs = User.objects.filter(username__iexact=username)
        if not user_qs.exists():
            status = 403
        else:
            user = user_qs.first()
            if sha256_crypt.verify(str(password), user.password):
                request.session['username'] = username
                status = 200
        res = {
            "username": username,
            "status": status,
        }
        return JsonResponse(res, safe=False)
        
    else:
        return HttpResponseBadRequest()


def registerUser(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = sha256_crypt.using(rounds=20000).hash(password)
        email = request.POST.get('email')
        status = 0
        if User.objects.filter(username__iexact=username).exists():
            status = 404
        else:
            new_user = User.objects.create(username=username, password=password, email=email, code_ids=[], code_title=[])
            new_user.save()
            request.session['username'] = username
            status = 200        
        res = {
            "status": status,
        }
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()


def logoutUser(request):
    if request.is_ajax():
        del request.session['username']
        res = {}
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()


def userExists(request):
    if request.is_ajax():
        username = request.GET.get('username')
        flag = 'True'
        user = User.objects.filter(username__iexact=username)
        if(user):
            flag = 'False'
        res = {
            "flag": flag,
        }
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()


def savetoProfile(request):
    return

def removefromProfile(request):
    return

def viewProfile(request):
    return