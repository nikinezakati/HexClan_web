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
    result={}
    result['followed_artists']=[]
    result['favorite_albums']=[]
    result['favorite_musics']=[]
    result['rating_musics']=[]
    result['rating_albums']=[]
    result['comment_artists']=[]
    result['comment_musics']=[]
    result['comment_albums']=[]

    user = request.user

    followed_artists = user.get_favorite_artists()
    for id in followed_artists:
        result['followed_artists'].append(get_artistname_by_id(id))

    favorite_albums = user.get_favorite_albums()
    for id in favorite_albums:
        result['favorite_albums'].append(get_albumname_by_id(id))

    favorite_musics = user.get_favorite_musics()
    for id in favorite_musics:
        result['favorite_musics'].append(get_recordingname_by_id(id)) 

    rating_musics = user.get_rating_musics()
    for id in rating_musics:
        result['rating_musics'].append(get_recordingname_by_id(id)) 

    rating_albums = user.get_rating_albums()
    for id in rating_albums:
        result['rating_albums'].append(get_albumname_by_id(id))     

    comment_artists = user.get_comment_artists()
    for id in comment_artists:
        result['comment_artists'].append(get_artistname_by_id(id))     

    comment_musics = user.get_comment_musics()
    for id in comment_musics:
        result['comment_musics'].append(get_recordingname_by_id(id))     

    comment_albums = user.get_comment_albums()
    for id in comment_albums:
        result['comment_albums'].append(get_albumname_by_id(id))                              


    return Response(result,status=status.HTTP_201_CREATED)
