from django.urls import path
from django.conf.urls import url
from .views import GenresAPIView


urlpatterns = [
    # path('test/', test),
    url(r'^genres/$',GenresAPIView.as_view()),
]    
