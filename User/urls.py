from django.urls import path
from . import views
from User.views import ProfileAPI, UpdateProfileView
from django.conf.urls import url


urlpatterns = [
    path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('update_profile/me/', ProfileAPI.as_view())
]
