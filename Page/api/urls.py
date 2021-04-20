from django.urls import path
from Page.api.views import *
from django.conf.urls import url

urlpatterns = [
	url(r'^ArtistSearchAPIView/$', ArtistSearchAPIView, name='ArtistSearchAPIView'),
	url(r'^MusicSearchAPIView/$', MusicSearchAPIView, name='MusicSearchAPIView'),
	url(r'^AlbumSearchAPIView/$', AlbumSearchAPIView, name='AlbumSearchAPIView')
]