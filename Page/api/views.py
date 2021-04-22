from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Page.models import page, Artist, Music, Album, URL
from Page.api.serializers import ArtistSerializer, MusicSerializer, AlbumSerializer
from musicbrainz.search_by_query import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_multiple_model.views import ObjectMultipleModelAPIView
from itertools import chain
from django.db.models import Q


@api_view(['GET', 'POST'])
def ArtistSearchAPIView(request):
	search = request.GET['search']
	results = search_artist_by_name(search)
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def MusicSearchAPIView(request):
	search = request.GET['search']
	results = search_recording_by_name(search)
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def AlbumSearchAPIView(request):
	search = request.GET['search']
	results = search_album_by_name(search)
	return Response(results, status=status.HTTP_201_CREATED)

