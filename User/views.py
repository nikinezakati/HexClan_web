from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from User.serializers import ProfileSerializer, UpdateAvatarUserSerializer, UpdateUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from musicbrainz.get_by_id import get_album_by_id, get_albumname_by_id, get_artist_by_id, get_artistname_by_id, get_recording_by_id, get_recordingname_by_id
from .models import *


User = get_user_model()


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = UpdateUserSerializer

    def get_object(self, queryset=None):
        return self.request.user


class ProfileAPI(APIView):
    def get(self, request, *args, **kwargs):
        user = request.user
        permission_classes = [IsAuthenticated,]
        profile_serializer = ProfileSerializer(user)
        return Response(profile_serializer.data)    

class UpdateAvatarProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = UpdateAvatarUserSerializer
    def get_object(self, queryset=None):
        return self.request.user


@api_view(['GET', ])
def ProfileInfoAPI(request):
    name = request.GET['username']
    result={}
    query=user.objects.all().filter(username=name)
    if len(query)>0:
        for q in query:
            if q.username==name:
                model=q
                result['followed_artists']=[]
                result['favorite_albums']=[]
                result['favorite_musics']=[]
                result['rating_musics']=[]
                result['rating_albums']=[]
                result['comment_artists']=[]
                result['comment_musics']=[]
                result['comment_albums']=[]
                

                result['username']=q.username
                result['first_name']=q.first_name
                result['last_name']=q.last_name
                result['last_name']=q.last_name
                result['email']=q.email
                result['description']=q.description
                try:
                    result['avatar']=q.avatar.url
                except:
                    result['avatar']=None
                followed_artists = model.get_favorite_artists()
                for id in followed_artists:
                    result['followed_artists'].append(get_artistname_by_id(id))

                favorite_albums = model.get_favorite_albums()
                for id in favorite_albums:
                    result['favorite_albums'].append(get_albumname_by_id(id))

                favorite_musics = model.get_favorite_musics()
                for id in favorite_musics:
                    result['favorite_musics'].append(get_recordingname_by_id(id)) 

                rating_musics = model.get_rating_musics()
                if len(rating_musics)>0:
                    for id in rating_musics:
                        temp={}
                        temp['music']=get_recordingname_by_id(id[0])
                        temp['rating']=id[1]
                        result['rating_musics'].append(temp) 

                rating_albums = model.get_rating_albums()
                if len(rating_albums)>0:
                    for id in rating_albums:
                        temp={}
                        temp['album']=get_albumname_by_id(id[0])
                        temp['rating']=id[1]
                        result['rating_albums'].append(temp)     

                comment_artists = model.get_comment_artists()
                if len(comment_artists)>0:
                    for id in comment_artists:
                        temp={}
                        temp['artist']=get_artistname_by_id(id[0])
                        temp['comment']=id[1]
                        temp['date']=id[2]
                        result['comment_artists'].append(temp)     

                comment_musics = model.get_comment_musics()
                if len(comment_musics)>0:
                    for id in comment_musics:
                        temp={}
                        temp['music']=get_recordingname_by_id(id[0])
                        temp['comment']=id[1]
                        temp['date']=id[2]
                        result['comment_musics'].append(temp)     

                comment_albums = model.get_comment_albums()
                if len(comment_albums)>0:
                    for id in comment_albums:
                        temp={}
                        temp['album']=get_albumname_by_id(id[0])
                        temp['comment']=id[1]
                        temp['date']=id[2]
                        result['comment_albums'].append(temp)                              

    return Response(result,status=status.HTTP_201_CREATED)
