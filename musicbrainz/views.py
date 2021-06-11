from .models import genre
from rest_framework import generics
from .search_by_query import search_artist_by_name
from rest_framework.decorators import api_view
from .ArtistSerializer import ArtistSerializer
from .AlbumSerializer import AlbumSerializer
from rest_framework import status
from rest_framework.response import Response
from User.models import *
from musicbrainz.genres import get_genres_mb
from rest_framework.permissions import IsAuthenticated
from musicbrainz.get_by_id import *
from .MusicSerializer import MusicSerializer


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
    result['musics_albums'] = browse_artist_music_by_id(artist_id) + browse_artist_album_by_id(artist_id)
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
    result['top_musics_albums'] = []
    i = 0
    for x in LIST:
        y = get_recording_by_id(x.music_id)
        result['top_musics_albums'].append(y)
        i += 1
        if i >= int(limit) or i >= len(LIST):
            break

    # topalbums
    LIST = total_album_rating.objects.filter(
        artist_id=artist_id).order_by('rating').reverse()

    i = 0
    for x in LIST:
        y = get_album_by_id(x.album_id)
        result['top_musics_albums'].append(y)
        i += 1
        if i >= int(limit) or i >= len(LIST):
            break

    # comments
    LIST = artist_comment.objects.filter(artist_id=artist_id)
    climit = request.GET['commentlimit']
    cpage = request.GET['commentpage']
    i = int(climit) * int(cpage)
    j = int(climit)
    result['comments'] = []
    while(j > 0):
        if(i >= len(LIST)):
            break
        d1 = {}
        d1['username'] = LIST[i].user.username
        d1['avatar'] = LIST[i].user.avatar.url
        d1['context'] = LIST[i].context
        d1['date'] = LIST[i].date
        result['comments'].append(d1)
        i = i + 1
        j = j - 1

    return Response(result, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def ArtistFollowAPI(request):
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
def ArtistUnfollowAPI(request):
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


@api_view(['GET'])
def AlbumAPIView(request):
    result = {}
    album_id = request.GET['id']

    album = AlbumSerializer()
    general_info = AlbumSerializer.general_info(album, id=album_id)
    result['general_info'] = general_info
    result['musics'] = browse_album_tracks_by_id(album_id)

    # comments
    LIST = album_comment.objects.filter(album_id=album_id)

    result['comments'] = []
    i = 0
    while(i < len(LIST)):
        d1 = {}
        d1['username'] = LIST[i].user.username
        try:
            d1['avatar'] = LIST[i].user.avatar.url
        except:
            d1['avatar'] = None
        d1['context'] = LIST[i].context
        d1['date'] = LIST[i].date
        result['comments'].append(d1)
        i = i + 1

    return Response(result, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def AlbumFavoriteAPI(request):
    result = {}
    album_id = request.GET['id']
    us = request.user
    if us.id != None:

        query = album_favorite.objects.all().filter(user=us, album_id=album_id)
        if len(query) == 0:
            ar = album_favorite.objects.create(album_id=album_id, user=us)
            result['msg'] = 'Succesful'

        else:
            result['msg'] = 'Album Already in Favorites'
    else:
        result['msg'] = 'User Not Signed in'

    return Response(result, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def AlbumUnfavoriteAPI(request):
    result = {}
    album_id = request.GET['id']
    us = request.user
    permission_classes = [IsAuthenticated, ]

    query = album_favorite.objects.all().filter(user=us, album_id=album_id)
    if len(query) > 0:
        ar = album_favorite.objects.all().filter(
           album_id=album_id, user=us).delete()
        result['msg'] = 'Succesful'

    else:
        result['msg'] = 'This Album is Not in Your Favorites'

    return Response(result, status=status.HTTP_201_CREATED)    


@api_view(['POST'])
def AlbumRateAPI(request):
    us = request.user
    album_id = request.GET['id']
    data = request.data
    if us.id != None:
        if(len(data) > 0):
            rate = data["rate"]
            if rate != None:
                album_rating.objects.create(
                    album_id=album_id, user=us, rating=float(rate))

            q = total_album_rating.objects.all().filter(album_id=album_id)
            if len(q) > 0:
                for l in q:
                    if l.album_id == album_id:
                        l.rating = ((l.rating*l.vote_num) +
                                    float(rate))/(l.vote_num+1)
                        l.vote_num += 1
                        l.save()
            else:
                artist_id = get_albumartist_by_id(album_id)
                total_album_rating.objects.create(
                    album_id=album_id, vote_num=1, rating=float(rate), artist_id=artist_id)
        else:
            data = {"msg": "no value for rating assigned"}
    else:
        data = {"msg": "you are not signed in"}
    return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def MusicAPIView(request):
    result = {}
    music_id = request.GET['id']

    music = MusicSerializer()
    general_info = MusicSerializer.general_info(music, id=music_id)
    result['general_info'] = general_info
    

    # comments
    LIST = music_comment.objects.filter(music_id=music_id)

    result['comments'] = []
    i = 0
    while(i < len(LIST)):
        d1 = {}
        d1['username'] = LIST[i].user.username
        try:
            d1['avatar'] = LIST[i].user.avatar.url
        except:
            d1['avatar'] = None
        d1['context'] = LIST[i].context
        d1['date'] = LIST[i].date
        result['comments'].append(d1)
        i = i + 1

    return Response(result, status=status.HTTP_201_CREATED)    

@api_view(['POST'])
def MusicFavoriteAPI(request):
    result = {}
    music_id = request.GET['id']
    us = request.user
    if us.id != None:

        query = music_favorite.objects.all().filter(user=us, music_id=music_id)
        if len(query) == 0:
            ar = music_favorite.objects.create(music_id=music_id, user=us)
            result['msg'] = 'Succesful'

        else:
            result['msg'] = 'Music Already in Favorites'
    else:
        result['msg'] = 'User Not Signed in'

    return Response(result, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def MusicUnfavoriteAPI(request):
    result = {}
    music_id = request.GET['id']
    us = request.user
    permission_classes = [IsAuthenticated, ]

    query = music_favorite.objects.all().filter(user=us, music_id=music_id)
    if len(query) > 0:
        ar = music_favorite.objects.all().filter(
           music_id=music_id, user=us).delete()
        result['msg'] = 'Succesful'


    else:
        result['msg'] = 'This Music is Not in Your Favorites'

    return Response(result, status=status.HTTP_201_CREATED)        

@api_view(['POST'])
def MusicRateAPI(request):
    us = request.user
    music_id = request.GET['id']
    data = request.data
    if us.id != None:
        if(len(data) > 0):
            rate = data["rate"]
            if rate != None:
                music_rating.objects.create(
                    music_id=music_id, user=us, rating=float(rate))

            q = total_music_rating.objects.all().filter(music_id=music_id)
            if len(q) > 0:
                for l in q:
                    if l.music_id == music_id:
                        l.rating = ((l.rating*l.vote_num) +
                                    float(rate))/(l.vote_num+1)
                        l.vote_num += 1
                        l.save()
            else:
                artist_id = get_musicartist_by_id(music_id)
                total_music_rating.objects.create(
                    music_id=music_id, vote_num=1, rating=float(rate), artist_id=artist_id)
        else:
            data = {"msg": "no value for rating assigned"}
    else:
        data = {"msg": "you are not signed in"}
    return Response(data, status=status.HTTP_201_CREATED)