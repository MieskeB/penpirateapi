from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'tool/index.html'