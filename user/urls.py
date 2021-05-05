from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('login', views.loginview, name='login'),
    path('register', views.registerview, name='register'),
    path('', views.account, name='account'),
    path('login/send', views.loginsend, name='login_send'),
    path('register/send', views.registersend, name='register_send'),
    path('logout', views.logoutsend, name='logout'),
    path('updatepassword', views.update_password, name='update_password')
]
