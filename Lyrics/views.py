from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from musicbrainz.search_by_query import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect, render
from musicbrainz.get_by_id import *
import requests
import json
from .models import *

@api_view(['GET', 'POST'])
def LyricsAPI(request):
	ID = request.GET['id']
	m = lyrics.objects.all().filter(music_id=ID)
	results={}
	results['results']=[]
	if len(m) == 0 :
		y = get_recording_lyrics(ID)
		run = "https://api.lyrics.ovh/v1/" + y['artist'][0]['name'] + "/" + y['title'] + "/"
		r = requests.get(run)
		print(r.text)
		if len(r.text) != 0:
			lyrics.objects.create(music_id=ID ,context=r.json())
			results['results'].append(r.json())
	else:
		r = m[0].context
		results['results'].append(r)
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def LyricsCommentAPI(request):
	user = request.user
	ID = request.GET['id']
	s = request.GET['start']
	e = request.GET['end']
	m = lyrics.objects.get(music_id=ID)
	data = request.data
	l = m.context['lyrics']
	section = l[int(s):int(e)]
	results = {}
	try:
		text = data["comment"]
	except:
		text = data
	if len(text) != 0:
			Commented_Section.objects.create(start_index=s, end_index=e, context=text, user=user, lyric=m)
			results['user']=user.id
			results['comment']=text
			results['section']=section
			results['lyric']=m.context['lyrics']

	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def LyricsALLCommentAPI(request):
	ID = request.GET['id']
	m = lyrics.objects.get(music_id=ID)
	LIST = Commented_Section.objects.all().filter(lyric=m)
	results={}
	results['results']=[]
	for x in LIST:
		d1={}
		d1['username']=x.user.username
		d1['userimage']=x.user.avatar.url
		d1['comment']=x.context
		l=x.lyric.context['lyrics']
		w=l[int(x.start_index):int(x.end_index)]
		d1['section']=w
		d1['date']=x.date
		results['results'].append(d1)
	return Response(results, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def LyricsTextCommentAPI(request):
	ID = request.GET['id']
	m = lyrics.objects.get(music_id=ID)
	LIST = Commented_Section.objects.all().filter(lyric=m).order_by('start_index')
	l = []
	b = False
	for x in LIST :
		for y in l:
			b = False
			if(x.start_index < y.end_index):
				b = True
				break
		if b == False:
			l.append(x)
	results={}
	results['results']=[]
	for x in l:
		d1={}
		d1['username']=x.user.username
		d1['userimage']=x.user.avatar.url
		d1['comment']=x.context
		d1['date']=x.date
		d1['start_index']=x.start_index
		d1['end_index']=x.end_index
		results['results'].append(d1)

	return Response(results, status=status.HTTP_201_CREATED)