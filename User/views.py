from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from User.serializers import UpdateUserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class UpdateProfileView(generics.UpdateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated,]
    serializer_class = UpdateUserSerializer

    def get_object(self, queryset=None):
        return self.request.user