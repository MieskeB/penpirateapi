from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def account(request):
    return render(request, 'user/account.html')


def loginview(request):
    return render(request, 'user/login.html')


def loginsend(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('user:account'))
    else:
        return HttpResponseRedirect(reverse('user:login'))


def registerview(request):
    return render(request, 'user/register.html')


def registersend(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username=username, email=email, password=password)
    user.save()

    login(request, user)

    return HttpResponseRedirect(reverse('user:account'))


@login_required
def update_password(request):
    try:
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request, 'user/account.html', {
                'error_message': 'password and confirmed password do not match',
            })
    except (KeyError, User.DoesNotExist):
        return render(request, 'user/account.html', {
            'error_message': 'Something went wrong',
        })
    else:
        u = request.user
        u.set_password(password)
        u.save()
        return HttpResponseRedirect(reverse('user:account'))


@login_required
def logoutsend(request):
    logout(request)
    return HttpResponseRedirect(reverse('user:account'))
