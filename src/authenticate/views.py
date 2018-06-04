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
            # stayloggedin = request.POST.get('stayloggedin')
            # if stayloggedin == "true":
            #     pass
            # else:
            #     request.session.set_expiry(0)

            message = "Invalid Credentials"
            temp = User.objects.all()
            print(temp)
            # user = User.objects.get(username=username)
            # print(user.password)
            # if user.password == password:
            #     request.session['username'] = username
            #     message = "Succesfully Logged in !!!"
            #     print(message)
            # users = User.objects
            # print(users)
            for user in temp:
                if username == user.username:
                    message = "Successfully logged in"
                    request.session['username'] = username
            res = {
                "msg": message,
                "username": username
            }
            print(res)
            return HttpResponse(json.dumps(res), content_type="application/json")
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
        if User.objects.get(username=username) or User.objects.get(email=email):
            message = "Username or Email already exists"
            flag = False
        
        if flag:
            new_user = User.objects.create(username=username, password=password, email=email, code_ids=[], code_title=[])
            new_user.save()
            request.session['username'] = username
            message = "Successfully created !!!"
        
        res = {
            "msg": message,
        }
        return JsonResponse(res, safe=False)
    else:
        return HttpResponseBadRequest()


def logoutUser(request):
    if request.is_ajax():
        del request.session['username']
        message = "Succesfully Logged out !!!"
        res = {
            "msg": message
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