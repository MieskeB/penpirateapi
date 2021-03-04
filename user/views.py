from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse

from .models import User


def index(request):
    users_list = User.objects.all()
    context = {
        'users_list': users_list,
    }
    return render(request, 'user/index.html', context)


def account(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'user/account.html', {'user': user})


def update_password(request, user_id):
    user = get_object_or_404(User, id=user_id)
    try:
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if (password != confirm_password):
            return render(request, 'user/account.html', {
                'user': user,
                'error_message': 'password and confirmed password do not match',
            })
    except (KeyError, User.DoesNotExist):
        return render(request, 'user/account.html', {
            'user': user,
            'error_message': 'Something went wrong',
        })
    else:
        user.password = password
        user.save()
        return HttpResponseRedirect(reverse('user:account', args=(user.id,)))