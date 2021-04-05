from django.urls import path
from . import views


urlpatterns = [

    path('', views.Home_page.Home, name = 'home'),
    path('signup/', views.Signup_page.Signup, name = 'signup'),
    path('login/', views.Login_page.Login, name = 'login'),
    path('logout/', views.Login_page.Logout, name = 'logout'),
    path('dashboard/<str:pk1>/', views.Dashboard_page.Dashboard),

]
