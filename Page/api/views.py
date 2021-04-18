from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from Page.models import page, Artist, Music, Album, URL
from Page.api.serializers import PageSerializer, ArtistSerializer, MusicSerializer, AlbumSerializer, URLSerializer

from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from drf_multiple_model.views import ObjectMultipleModelAPIView
from itertools import chain
from django.db.models import Q


@api_view(['GET', 'POST'])
def SearchAPIView(request):
	search = request.GET['search']
	artist = Artist.objects.filter(Q(name__icontains= search) | Q(artist_type__icontains = search) | Q(albums__name__icontains = search)).distinct()
	music = Music.objects.filter(Q(artists__name__icontains = search) | Q(genre__icontains = search) | Q(music_album__name__icontains = search)).distinct()
	album = Album.objects.filter(Q(name__icontains = search) | Q(music__name__icontains = search) | Q(artist__name__icontains = search)).distinct()
	artist_serializer = ArtistSerializer(artist, many = True)
	music_serializer = MusicSerializer(music, many = True)
	album_serializer = AlbumSerializer(album, many = True)
	results = artist_serializer.data + music_serializer.data + album_serializer.data
	return Response(results, status=status.HTTP_201_CREATED)