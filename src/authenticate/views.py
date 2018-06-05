from django.shortcuts import render
from django.http import HttpResponseBadRequest, JsonResponse, HttpResponse
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
            try:
                user = User.objects.get(username=username)
            except:
                message = "Invalid Credentials"
            print(user.password)
            if user.password == password:
                request.session['username'] = username
                message = "Succesfully Logged in !!!"
                print(message)            
            res = {
                "msg": message,
                "username": username,
                "status": 200
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
        email = request.POST.get('email')
        flag = True
        message = ""
        print("stage 1")
        try:
            if User.objects.get(username=username) or User.objects.get(email=email):
                message = "Username or Email already exists"
                flag = False
        except:
            pass
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