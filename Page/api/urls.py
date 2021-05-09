from django.urls import path
from Page.api.views import *
from django.conf.urls import url

urlpatterns = [
	path('TenTopArtistAPIView/', TenTopArtistAPIView, name = 'TenTopArtistAPIView'),
	path('TenTopMusicAPIView/', TenTopMusicAPIView, name = 'TenTopMusicAPIView'),
	path('TenTopAlbumAPIView/', TenTopAlbumAPIView, name = 'TenTopAlbumAPIView'),
	url(r'^ArtistSearchAPIView/$', ArtistSearchAPIView, name='ArtistSearchAPIView'),
	url(r'^MusicSearchAPIView/$', MusicSearchAPIView, name='MusicSearchAPIView'),
	url(r'^AlbumSearchAPIView/$', AlbumSearchAPIView, name='AlbumSearchAPIView')
]