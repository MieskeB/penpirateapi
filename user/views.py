from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import User


class IndexView(generic.ListView):
    template_name = 'user/index.html'
    context_object_name = 'users_list'

    def get_queryset(self):
        return User.objects.all()


class AccountView(generic.DetailView):
    model = User
    template_name = 'user/account.html'


def update_password(request, user_id):
    user = get_object_or_404(User, pk=user_id)
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
