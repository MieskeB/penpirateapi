from django.shortcuts import render


def index(request):
    return render(request, 'tutorial/index.html')


def monitoring(request):
    return render(request, 'tutorial/monitoring.html')


def pentesting(request):
    return render(request, 'tutorial/pentesting.html')


def riskanalysis(request):
    return render(request, 'tutorial/riskanalysis.html')
