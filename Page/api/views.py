from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Page.models import page, Artist, Music, Album, URL
#from Page.api.serializers import ArtistSerializer, MusicSerializer, AlbumSerializer
from musicbrainz.search_by_query import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
#from drf_multiple_model.views import ObjectMultipleModelAPIView
from itertools import chain
from django.db.models import Q
from User.models import *

@api_view(['GET', 'POST'])
def ArtistSearchAPIView(request):
	search = request.GET['search']
	limit = request.GET['limit']
	page = request.GET['page']
	offset = (int(limit)+1)*int(page)
	results = search_artist_by_name(search, limit, str(offset))
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def MusicSearchAPIView(request):
	search = request.GET['search']
	limit = request.GET['limit']
	page = request.GET['page']
	offset = (int(limit)+1)*int(page)
	results = search_recording_by_name(search, limit, str(offset))
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def AlbumSearchAPIView(request):
	search = request.GET['search']
	limit = request.GET['limit']
	page = request.GET['page']
	offset = (int(limit)+1)*int(page)
	results = search_album_by_name(search, limit, str(offset))
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def TenTopArtistAPIView(request):
	LIST = top_artist_rating.objects.all().order_by('rating').reverse()
	results=[]
	i=0
	for x in LIST:
		y = top_artists(x.artist_id)
		results.append(y)
		i += 1
		if i >= 10 or i >= len(LIST):
			break
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def TenTopMusicAPIView(request):
	LIST = top_music_rating.objects.all().order_by('rating').reverse()
	results=[]
	i=0
	for x in LIST:
		y = top_musics(x.music_id)
		results.append(y)
		i += 1
		if i >= 10 or i >= len(LIST):
			break
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def TenTopAlbumAPIView(request):
	LIST = top_album_rating.objects.all().order_by('rating').reverse()
	results=[]
	i=0
	for x in LIST:
		y = top_albums(x.album_id)
		results.append(y)
		i += 1
		if i >= 10 or i >= len(LIST):
			break
	return Response(results, status=status.HTTP_201_CREATED)