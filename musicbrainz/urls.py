from django.urls import path
from django.conf.urls import url
from .views import *

urlpatterns = [
    # path('test/', test),
    url(r'^genres/$',GenresAPIView.as_view()),
	path('gdb/', gdb, name = 'gdb'),
]    
