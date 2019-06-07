from django.shortcuts import render, redirect, HttpResponse
from repository import models
from django.contrib.auth.models import Group, Permission
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User


# def test(request):
#     user = User.objects.create_user(username='12345', password='12345', email='2@qq.com')
# user = User.objects.filter(id=5).first()
# per = Permission.objects.filter(id=3)
# user.user_permissions.add("Can add session")
# print(user.)
# print("hello world")
# print(user)
# str = '123'
# if user.has_perm('add_logentry'):
#   str='234'
# else:
#    str='456'

def do_login(request):
    if request.method == 'GET':
        return render(request, 'backend/login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
            # Redirect to a success page.

        else:
            # Return an 'invalid login' error message.
            return render(request, 'backend/login.html')


def do_logout(request):
    logout(request)
    return render(request, 'backend/login.html')