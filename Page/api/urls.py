from django.urls import path
from Page.api.views import SearchAPIView
from django.conf.urls import url

urlpatterns = [
	url(r'^SearchAPIView/$', SearchAPIView, name='SearchAPIView')

]