from django.urls import path
from . import views
from User.views import ProfileAPI, ProfileInfoAPI, UpdateAvatarProfileView, UpdateProfileView
from django.conf.urls import url


urlpatterns = [
    path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('update_profile/me/', ProfileAPI.as_view()),
    path('update_avatar_profile/', UpdateAvatarProfileView.as_view()),
    url(r'^ProfileInfoAPI/$', ProfileInfoAPI, name='ProfileInfoAPI'),
]
