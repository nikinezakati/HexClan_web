from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from User.serializers import ProfileSerializer, UpdateUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

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
        profile_serializer = ProfileSerializer(user)
        return Response(profile_serializer.data)    

