from django.urls import path

from . import views

app_name = 'tutorial'
urlpatterns = [
    path('', views.index, name='index'),
    path('monitoring', views.monitoring, name='monitoring'),
    path('pentesting', views.pentesting, name='pentesting'),
    path('riskanalysis', views.riskanalysis, name='riskanalysis')
]
