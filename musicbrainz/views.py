from .models import genre
from .GenreSerializer import GenreSerializer
from rest_framework import generics

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
    
    