from .models import genre
from rest_framework import generics
from .search_by_query import search_artist_by_name
from rest_framework.decorators import api_view
from .ArtistSerializer import ArtistSerializer
from rest_framework import status
from rest_framework.response import Response
from User.models import album_favorite, artist_favorite, total_artist_followings
from musicbrainz.genres import get_genres_mb
from rest_framework.permissions import IsAuthenticated
from musicbrainz.get_by_id import *


@api_view(['GET'])
def test(request):
    search_artist_by_name('Billie Eilish', 0, 0, True)


@api_view(['GET', ])
def gdb(request):
    get_genres_mb()
    return Response(status=status.HTTP_201_CREATED)


@api_view(['GET'])
def ArtistAPIView(request):
    result = {}
    result['me_follow'] = 'False'
    artist_id = request.GET['id']
    result['musics'] = browse_artist_music_by_id(artist_id)
    result['albums'] = browse_artist_album_by_id(artist_id)
    artist = ArtistSerializer()
    general_info = ArtistSerializer.general_info(artist, id=artist_id)
    result['general_info'] = general_info
    us = request.user
    if us.id != None:
        query = artist_favorite.objects.all().filter(user=us)
        if len(query) > 0:
            for q in query:
                if q.artist_id == artist_id:
                    result['me_follow'] = 'True'
                else:
                    result['me_follow'] = 'False'
        else:
            result['me_follow'] = 'False'
    # topmusics
    limit = request.GET['limit']
    LIST = total_music_rating.objects.filter(
        artist_id=artist_id).order_by('rating').reverse()
    result['top_musics'] = []
    i = 0
    for x in LIST:
        y = get_recording_by_id(x.music_id)
        result['top_musics'].append(y)
        i += 1
        if i >= int(limit) or i >= len(LIST):
            break

    # topalbums
    LIST = total_album_rating.objects.filter(
        artist_id=artist_id).order_by('rating').reverse()

    result['top_albums'] = []
    i = 0
    for x in LIST:
        y = get_album_by_id(x.album_id)
        result['results'].append(y)
        i += 1
        if i >= int(limit) or i >= len(LIST):
            break

    return Response(result, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def ArtistFollowAPIView(request):
    result = {}
    artist_id = request.GET['id']
    us = request.user
    if us.id != None:

        query = artist_favorite.objects.all().filter(user=us, artist_id=artist_id)
        if len(query) == 0:
            ar = artist_favorite.objects.create(artist_id=artist_id, user=us)
            result['msg'] = 'Succesful'

            q = total_artist_followings.objects.all().filter(artist_id=artist_id)
            if len(q) > 0:
                for l in q:
                    if l.artist_id == artist_id:
                        l.following_num += 1
                        l.save()
            else:
                total_artist_followings.objects.create(
                    artist_id=artist_id, following_num=1)
        else:
            result['msg'] = 'Already Following this Artist'
    else:
        result['msg'] = 'User Not Signed in'

    return Response(result, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def ArtistUnfollowAPIView(request):
    result = {}
    artist_id = request.GET['id']
    us = request.user
    permission_classes = [IsAuthenticated, ]

    query = artist_favorite.objects.all().filter(user=us, artist_id=artist_id)
    if len(query) > 0:
        ar = artist_favorite.objects.all().filter(
            artist_id=artist_id, user=us).delete()
        result['msg'] = 'Succesful'

        q = total_artist_followings.objects.all().filter(artist_id=artist_id)
        if len(q) > 0:
            for l in q:
                if l.artist_id == artist_id:
                    l.following_num -= 1
                    l.save()

    else:
        result['msg'] = 'Not Following this Artist'

    return Response(result, status=status.HTTP_201_CREATED)
