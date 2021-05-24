from .models import genre
from .GenreSerializer import GenreSerializer
from rest_framework import generics
import wikipedia
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .genres import *
# @api_view(['GET'])
# def test(request):
    

# @api_view(['GET'])
# @renderer_classes([JSONRenderer]) 
# def GenresApi(request, *args, **kwargs): 
#     qs = genre.objects.all()
#     serializer = GenreSerializer()
#     return Response(serializer.data) 


class GenresAPIView(generics.ListAPIView):
    queryset = genre.objects.all()
    serializer_class = GenreSerializer

@api_view(['GET',])
def gdb(request):
	get_genres_mb()
	return Response(status=status.HTTP_201_CREATED)
