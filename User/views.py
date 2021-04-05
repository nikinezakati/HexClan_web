from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import userSerializer
from .models import user 
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, Http404

@api_view(['GET'])
def Home(request):
	api_urls = {

		'List' : '/user-list/',
		'Log in' : '/user-login/',
		'Sign up' : '/user-signup/',
		
	}
	return Response(api_urls)

@api_view(['GET'])
def userList(request):
	users = user.objects.all()
	serializer = userSerializer(users, many = True)
	return Response(serializer.data)

@api_view(['POST'])
def userLogin(request):
	if request.method == 'POST':
		username = request.data["username"]
		if(username == "logout"):
			Logout(request)
		password = request.data["password"]
		u = authenticate(request, username=username, password=password)
		if u is not None:
			login(request, u)
			users = user.objects.get(username = username)
			serializer = userSerializer(users, many = False)
			return Response(serializer.data)
		else:
			raise Http404

@api_view(['POST'])
def userSignup(request):
	serializer = userSerializer(data = request.data)
	if serializer.is_valid():
		serializer.save()
		return Response(serializer.data)
	else:
		raise Http404

def Logout(request):
        logout(request)