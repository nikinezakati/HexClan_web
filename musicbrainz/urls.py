from django.urls import path
from django.conf.urls import url
from .views import test,ArtistAPIView
from musicbrainz.views import ArtistFollowAPIView, ArtistUnfollowAPIView, gdb


urlpatterns = [
    path('test/', test),
    path('gdb/', gdb, name = 'gdb'),
    url(r'^ArtistAPIView/$', ArtistAPIView, name='ArtistAPIView'),
    url(r'^ArtistFollowAPIView/$', ArtistFollowAPIView, name='ArtistFollowAPIView'),
    url(r'^ArtistUnfollowAPIView/$', ArtistUnfollowAPIView, name='ArtistUnfollowAPIView'),
]    
