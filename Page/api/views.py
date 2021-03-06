from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from Page.models import page, Artist, Music, Album, URL
# from Page.api.serializers import ArtistSerializer, MusicSerializer, AlbumSerializer
from musicbrainz.search_by_query import *
from rest_framework.generics import ListAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
# from drf_multiple_model.views import ObjectMultipleModelAPIView
from itertools import chain
from django.db.models import Q
from User.models import *
from musicbrainz.get_by_id import *
from musicbrainz.models import genre


@api_view(['GET', 'POST'])
def ArtistSearchAPIView(request):
	search = request.GET['search']
	limit = request.GET['limit']
	page = request.GET['page']
	photo = request.GET['photo']
	offset = (int(limit)+1)*int(page)
	if photo == 'True':
		results = search_artist_by_name(search, limit, str(offset), photo=True)
	if photo == 'False':
		results = search_artist_by_name(search, limit, str(offset), photo=False)
	return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def MusicSearchAPIView(request):
	search = request.GET['search']
	limit = request.GET['limit']
	page = request.GET['page']
	photo = request.GET['photo']
	offset = (int(limit)+1)*int(page)
	if photo == 'True':
		results = search_recording_by_name(search, limit, str(offset), photo=True)
	if photo == 'False':
		results = search_recording_by_name(search, limit, str(offset), photo=False)
	return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def AlbumSearchAPIView(request):
	search = request.GET['search']
	limit = request.GET['limit']
	page = request.GET['page']
	photo = request.GET['photo']
	offset = (int(limit)+1)*int(page)
	if photo == 'True':
		results = search_album_by_name(search, limit, str(offset), photo=True)
	if photo == 'False':
		results = search_album_by_name(search, limit, str(offset), photo=False)
	return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def TenTopArtistAPIView(request):
	LIST = total_artist_followings.objects.all().order_by('following_num').reverse()
	results = []
	i = 0
	for x in LIST:
		y = get_artist_by_id(x.artist_id)
		if len(y)!=0:
			y['rank'] = i + 1
			i += 1
			results.append(y)
		if i >= 10 or i >= len(LIST):
			break
	return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def TenTopMusicAPIView(request):
	LIST = total_music_rating.objects.all().order_by('rating').reverse()
	results = []
	i = 0
	for x in LIST:
		y = get_recording_by_id(x.music_id)
		if len(y)!=0:
			y['rank'] = i + 1
			i += 1
			results.append(y)
		if i >= 10 or i >= len(LIST):
			break
	return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def TenTopAlbumAPIView(request):
	LIST = total_album_rating.objects.all().order_by('rating').reverse()
	results = []
	i = 0
	for x in LIST:
		y = get_album_by_id(x.album_id)
		if len(y)!=0:
			y['rank'] = i + 1
			i += 1
			results.append(y)
		if i >= 10 or i >= len(LIST):
			break
	return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def SuggestionSearchAPIView(request):
  search = request.GET['search']
  results = {}
  results['results'] = []
  d1 = {}
  d1['name'] = "Artist"

  r1 = {}
  r1['name'] = "Artists"
  r1['results'] = []
  temp1 = search_artist_by_name(
      search, limit=3, offset=0, photo=False)['results']
  for t in temp1:
    if 'name' in t:
      d = {}
      d['title'] = t['name']
      r1['results'].append(d)

  if len(r1['results']) > 0:
    results['results'].append(r1)

  r2 = {}
  r2['name'] = "Albums"
  r2['results'] = []
  temp2 = search_album_by_name(
      search, limit=3, offset=0, photo=False)['results']
  for t in temp2:
    if 'title' in t:
      d = {}
      d['title'] = t['title']
      r2['results'].append(d)

  if len(r2['results']) > 0:
    results['results'].append(r2)

  r3 = {}
  r3['name'] = "Tracks"
  r3['results'] = []
  temp3 = search_recording_by_name(
      search, limit=3, offset=0, photo=False)['results']
  for t in temp3:
    if 'title' in t:
      d = {}
      d['title'] = t['title']
      r3['results'].append(d)

  if len(r3['results']) > 0:
    results['results'].append(r3)

  return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET', ])
def GenreAPIView(request):
	LIST = genre.objects.all().order_by('id')
	limit = request.GET['limit']
	page = request.GET['page']
	i = int(limit) * int(page)
	j = int(limit)
	results = {}
	results['results'] = []
	while(j > 0):
		if(i >= len(LIST)):
			break
		d1 = {}
		d1['name'] = LIST[i].name
		d1['description'] = LIST[i].description
		results['results'].append(d1)
		i = i + 1
		j = j - 1
	return Response(results, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def GenrePageAPIView(request):
	result={}
	name = request.GET['name']
	result=get_genres_releases(name)
	return Response(result, status=status.HTTP_201_CREATED)	
	
@api_view(['GET', 'POST'])
def ArtistCommentAPI(request):
	user = request.user
	artistid = request.GET['id']
	data = request.data
	try:
		text = data["comment"]
		if len(text) != 0:
			artist_comment.objects.create(artist_id=artistid.strip(),user=user, context=text)
	except:
		text = data
	return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def AlbumCommentAPI(request):
	us = request.user
	albumid = request.GET['id']
	data = request.data
	if us.id!=None:

		if(len(data)>0):
			text = data["comment"]
			if len(text) != 0:
				album_comment.objects.create(album_id=albumid ,user=us, context=text)
		else:
			text = data
	else:
		data={"msg": "you are not signed in"}			
	return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'POST'])
def MusicCommentAPI(request):
	us = request.user
	musicid = request.GET['id']
	data = request.data
	if us.id!=None:

		if(len(data)>0):
			text = data["comment"]
			if len(text) != 0:
				music_comment.objects.create(music_id=musicid ,user=us, context=text)
		else:
			text = data
	else:
		data={"msg": "you are not signed in"}			
	return Response(data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def LatestUserCommentAPI(request):
	username = request.GET['username']
	LIST = user.objects.get(username=username)
	artistcom = artist_comment.objects.all().filter(user_id=LIST.id).order_by('date')
	musiccom = music_comment.objects.all().filter(user_id=LIST.id).order_by('date')
	albumcom = album_comment.objects.all().filter(user_id=LIST.id).order_by('date')
	all_list = sorted(chain(artistcom, musiccom, albumcom), key=lambda car: car.date, reverse=True)
	print(len(artistcom))
	results={}
	results['results'] = []
	i = 0
	for x in all_list:
		d1 = {}
		try:
			d1['artist id'] = x.artist_id
		except:
			pass
		try:
			d1['music id'] = x.music_id
		except:
			pass
		try:
			d1['album id'] = x.album_id
		except:
			pass
		d1['comment'] = x.context
		d1['date'] = x.date
		results['results'].append(d1)
		i += 1
		if(i>=5):
			break
	return Response(results, status=status.HTTP_201_CREATED)



