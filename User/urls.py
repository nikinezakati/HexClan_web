from django.urls import path
from . import views
from User.views import UpdateProfileView
from django.conf.urls import url


urlpatterns = [
    path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
]
