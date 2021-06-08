from django.urls import path
from django.conf.urls import url
from .views import test,ArtistAPIView
from musicbrainz.views import *


urlpatterns = [
    path('test/', test),
    path('gdb/', gdb, name = 'gdb'),
    url(r'^ArtistAPIView/$', ArtistAPIView, name='ArtistAPIView'),
    url(r'^ArtistFollowAPI/$', ArtistFollowAPI, name='ArtistFollowAPI'),
    url(r'^ArtistUnfollowAPI/$', ArtistUnfollowAPI, name='ArtistUnfollowAPI'),
    url(r'^AlbumAPIView/$', AlbumAPIView, name='AlbumAPIView'),
    url(r'^AlbumFavoriteAPI/$', AlbumFavoriteAPI, name='AlbumFavoriteAPI'),
    url(r'^AlbumUnfavoriteAPI/$', AlbumUnfavoriteAPI, name='AlbumUnfavoriteAPI'),
    url(r'^AlbumRateAPI/$', AlbumRateAPI, name='AlbumRateAPI'),
    url(r'^MusicAPIView/$', MusicAPIView, name='MusicAPIView'),
    url(r'^MusicFavoriteAPI/$', MusicFavoriteAPI, name='MusicFavoriteAPI'),
    url(r'^MusicUnfavoriteAPI/$', MusicUnfavoriteAPI, name='MusicUnfavoriteAPI'),
    url(r'^MusicRateAPI/$', MusicRateAPI, name='MusicRateAPI'),
]    
