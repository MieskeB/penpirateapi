from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:user_id>/', views.account, name='account'),
    path('<int:user_id>/updatepassword/', views.update_password, name='update_password')
]