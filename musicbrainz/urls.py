from django.urls import path
from django.conf.urls import url
from .views import GenresAPIView,test,ArtistAPIView
from musicbrainz.views import ArtistFollowAPIView


urlpatterns = [
    path('test/', test),
    url(r'^genres/$',GenresAPIView.as_view()),
    url(r'^ArtistAPIView/$', ArtistAPIView, name='ArtistAPIView'),
    url(r'^ArtistFollowAPIView/$', ArtistFollowAPIView, name='ArtistFollowAPIView'),
]    
