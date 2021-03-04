from django.http import HttpResponse;


def index(request):
    return HttpResponse("Hello, world. You're at the user index")


def account(request, user_id):
    return HttpResponse("You're looking at an account with id %s." % user_id)
