# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from base.models.new_user import NewUser
from django.contrib.auth.models import User
import json

try:
    from django.apps import apps as models
except ImportError:  # django < 1.7
    from django.db import models




def index(request):
    return render(request, 'index.html')


def get_login(request):
    '''
    获取登陆页
    :param request:
    :return:
    '''
    return render(request, 'login.html')


def alogin(request):
    '''
    登陆页面
    :param request:
    :param args:
    :param kwargs:
    :return:
    '''
    username = request.POST['username']
    password = request.POST['password']
    try:
        User.objects.get(username=username)
    except:
        return render(request, 'login.html', {'error_msg': u"账户不存在"})
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponseRedirect('/mycenter/note/create/')
        # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            return render(request, 'login.html',{"error_msg":u'账户被禁用'})
    else:
        return render(request, 'login.html',{"error_msg":u'密码错误'})


def loginout(request):
    '''
    退出登录页
    :param request:
    :return:
    '''
    logout(request)
    return render(request, 'index.html')

def to_register(request):
    return render(request, 'register.html')

def register(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username=username,password=password)
    # user = User.objects.create_user(username,'',password)
    # user.last_name = 'Lennon'
    user.save()
    login(request, user)
    return render(request, 'index.html')



