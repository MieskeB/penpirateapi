from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.AccountView.as_view(), name='account'),
    path('<int:user_id>/updatepassword/', views.update_password, name='update_password')
]