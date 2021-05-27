from .models import genre
from rest_framework import generics
from .search_by_query import search_artist_by_name
from rest_framework.decorators import api_view
from .ArtistSerializer import ArtistSerializer
from rest_framework import status
from rest_framework.response import Response
from User.models import album_favorite, artist_favorite, total_artist_followings
from musicbrainz.genres import get_genres_mb

@api_view(['GET'])
def test(request):
    search_artist_by_name('Billie Eilish',0,0,True)
    

@api_view(['GET',])
def gdb(request):
    get_genres_mb()
    return Response(status=status.HTTP_201_CREATED)    

@api_view(['GET'])
def ArtistAPIView(request):
    result={}
    result['me_follow']=''
    artist_id = request.GET['id']
    artist=ArtistSerializer()
    general_info = ArtistSerializer.general_info(artist,id=artist_id)
    result ['general_info'] = general_info  
    us = request.user
    if us.id != None:
        query=artist_favorite.objects.all().filter(user=us)
        if len(query) > 0:
            for q in query:
                if q.artist_id==artist_id:
                    result['me_follow']='True'
                else:
                    result['me_follow']='False'  
        else:             
            result['me_follow']='False'  
    return Response(result, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def ArtistFollowAPIView(request):
    result={}
    artist_id = request.GET['id']
    us = request.user
    if us.id != None:

        query=artist_favorite.objects.all().filter(user=us,artist_id=artist_id)
        if len(query)==0:
            ar=artist_favorite.objects.create(artist_id=artist_id,user=us)
            result['msg']='Succesful'
            
            q=total_artist_followings.objects.all().filter(artist_id=artist_id)
            if len(q) > 0:
                for l in q:
                    if l.artist_id== ar:
                        l.following_num+=1
            else:
                total_artist_followings.objects.create(artist_id=artist_id,following_num=1)
        else:
            result['msg']='Already Following this Artist'       
    else:
        result['msg']='User Not Signed in'        

    return Response(result, status=status.HTTP_201_CREATED)            

    