from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
from passlib.hash import sha256_crypt
import json

from .models import User

def loginUser(request):
    if request.is_ajax():
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            print(username)
            print(password)
            stayloggedin = request.POST.get('stayloggedin')
            if stayloggedin == "true":
                pass
            else:
                request.session.set_expiry(0)

            message = "Invalid Credentials"
            temp = User.objects.all()
            print(temp)            
            user_qs = User.objects.filter(username__iexact=username)
            print(user_qs)
            if not user_qs.exists():
                message = "Invalid Credentials"
                status = 403
            else:
                user = user_qs.first()
                print(user)
                print("here")
                # print(user.password)
                print(sha256_crypt.verify(str(password), user.password))
                if sha256_crypt.verify(str(password), user.password):
                    request.session['username'] = username
                    message = "Succesfully Logged in !!!"
                    print(message)            
                    status = 200
            res = {
                "msg": message,
                "username": username,
                "status": status,
            }
            print(res)
            return JsonResponse(res, safe=False)
        except Exception as e:
            print (e)
    else:
        return HttpResponseBadRequest()


def registerUser(request):
    if request.is_ajax():
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = sha256_crypt.using(rounds=20000).hash(password)
        email = request.POST.get('email')
        flag = True
        message = ""
        print("stage 1")
        if User.objects.filter(username__iexact=username).exists():
            message = "Username already exists"
            flag = False
        print("stage 2")
        if flag:
            new_user = User.objects.create(username=username, password=password, email=email, code_ids=[], code_title=[])
            new_user.save()
            request.session['username'] = username
            message = "Successfully created !!!"
        
        res = {
            "msg": message,
        }
        print(res)
        print("Stage 3")
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()


def logoutUser(request):
    if request.is_ajax():
        print(request.session['username'])
        del request.session['username']
        message = "Succesfully Logged out !!!"
        print(message)
        res = {
            "msg": message
        }
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()


def userExists(request):
    if request.is_ajax():
        username = request.GET.get('username')
        # print(username)
        flag = 'True'
        user = User.objects.filter(username__iexact=username)
        print(user.exists())
        print(len(username))
        if(user):
            flag = 'False'
        res = {
            "flag": flag,
        }
        print(res)
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()


def savetoProfile(request):
    return

def removefromProfile(request):
    return

def viewProfile(request):
    return