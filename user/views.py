from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render

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
