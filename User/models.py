from django.db import models
from Page.models import *
from django.contrib.auth.models import AbstractUser

class user(AbstractUser):
    description       = models.CharField(max_length=255, default='', null = True, blank = True)
    avatar            = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, null = True, blank = True)
    music_ratings     = models.ManyToManyField(Music, null = True, blank = True, )
    album_ratings     = models.ManyToManyField(Album,related_name='user_albumrating', null = True, blank = True)
    favorites_musics  = models.ManyToManyField(Music,related_name='user_favoritemusic', null = True, blank = True)
    favorites_albums  = models.ManyToManyField(Album, null = True, blank = True)
    favorites_artists = models.ManyToManyField(Artist, null = True, blank = True)

    def __str__(self):
        return self.username

class Comment(models.Model):
    page    = models.ForeignKey(page,on_delete=models.CASCADE,null=True)
    user    = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    context = models.CharField(max_length=255,default='')

class Like(models.Model):
    page    = models.ForeignKey(page,on_delete=models.CASCADE,null=True)
    user    = models.ForeignKey(user,on_delete=models.CASCADE,null=True)