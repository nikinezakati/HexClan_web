from django.urls import path
from Page.api.views import *
from django.conf.urls import url

urlpatterns = [
	path('TenTopArtistAPIView/', TenTopArtistAPIView, name = 'TenTopArtistAPIView'),
	path('TenTopMusicAPIView/', TenTopMusicAPIView, name = 'TenTopMusicAPIView'),
	path('TenTopAlbumAPIView/', TenTopAlbumAPIView, name = 'TenTopAlbumAPIView'),
	url(r'^ArtistSearchAPIView/$', ArtistSearchAPIView, name='ArtistSearchAPIView'),
	url(r'^MusicSearchAPIView/$', MusicSearchAPIView, name='MusicSearchAPIView'),
	url(r'^AlbumSearchAPIView/$', AlbumSearchAPIView, name='AlbumSearchAPIView'),
	url(r'^SuggestionSearchAPIView/$', SuggestionSearchAPIView, name='SuggestionSearchAPIView'),
	url(r'^ArtistCommentAPI/$', ArtistCommentAPI, name='ArtistCommentAPI'),
	#url(r'^ArtistAllCommentAPI/$', ArtistAllCommentAPI, name='ArtistAllCommentAPI'),
	url(r'^GenreAPIView/$', GenreAPIView, name='GenreAPIView'),
	#url(r'^ArtistMusicsAPIView/$', ArtistMusicsAPIView, name='ArtistMusicsAPIView'),
	#url(r'^ArtistAlbumsAPIView/$', ArtistAlbumsAPIView, name='ArtistAlbumsAPIView'),
	#url(r'^ArtistTopMusicsAPIView/$', ArtistTopMusicsAPIView, name='ArtistTopMusicsAPIView'),
	#url(r'^ArtistTopAlbumsAPIView/$', ArtistTopAlbumsAPIView, name='ArtistTopAlbumsAPIView'),
]