from django.urls import path
from . import views


urlpatterns = [

    path('', views.Home, name = "home"),
    path('user-list/', views.userList, name = "user-list"),
    path('user-login/', views.userLogin, name = "user-login"),
    path('user-signup/', views.userSignup, name = "user-signup"),
]