from django.urls import path
from . import views
from User.views import UpdateProfileView
from django.conf.urls import url


urlpatterns = [
<<<<<<< HEAD
    path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
=======

    
>>>>>>> 9714b8cf6127e11216882da5cb200b53b27c2126
]