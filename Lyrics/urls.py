from django.urls import path
from .views import *
from django.conf.urls import url

urlpatterns = [
	url(r'^LyricsAPI/$', LyricsAPI, name='LyricsAPI'),
	url(r'^LyricsCommentAPI/$', LyricsCommentAPI, name='LyricsCommentAPI'),
	url(r'^LyricsALLCommentAPI/$', LyricsALLCommentAPI, name='LyricsALLCommentAPI'),
	url(r'^LyricsTextCommentAPI/$', LyricsTextCommentAPI, name='LyricsTextCommentAPI'),
]