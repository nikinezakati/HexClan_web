from django.urls import path
from . import views
from User.views import ProfileAPI, UpdateProfileView, UpdateAvatarProfileView
from django.conf.urls import url


urlpatterns = [
    path('update_profile/', UpdateProfileView.as_view(), name='auth_update_profile'),
    path('update_profile/me/', ProfileAPI.as_view()),
    path('update_avatar_profile/', UpdateAvatarProfileView.as_view()),
    #path('profile_info/me/', ProfileInfoAPI.as_view())
]
