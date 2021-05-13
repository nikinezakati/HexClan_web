from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class user(AbstractUser):
    description       = models.CharField(max_length=255, default='', null = True, blank = True)
    avatar            = models.ImageField(upload_to='Images/', height_field=None, width_field=None, max_length=100, null = True, blank = True)
    music_ratings     = models.ManyToManyField('music_rating',related_name='+' )
    album_ratings     = models.ManyToManyField('album_rating',related_name='+')
    artist_ratings    = models.ManyToManyField('artist_rating',related_name='+')
    favorites_musics  = models.ManyToManyField('music_favorite',related_name='+')
    favorites_albums  = models.ManyToManyField('album_favorite',related_name='+')
    favorites_artists = models.ManyToManyField('artist_favorite',related_name='+')
    REQUIRED_FIELDS   = ['email', 'first_name', 'last_name',]
      
    def __str__(self):
        return self.username

class music_comment(models.Model):
    music_id = models.CharField(max_length=255,default='')
    user     = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    context  = models.CharField(max_length=255,default='')

class album_comment(models.Model):
    album_id = models.CharField(max_length=255,default='')
    user     = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    context  = models.CharField(max_length=255,default='')

class artist_comment(models.Model):
    artist_id = models.CharField(max_length=255,default='')
    user      = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    context   = models.CharField(max_length=255,default='')

class music_like(models.Model):
    music_id = models.CharField(max_length=255,default='')
    user     = models.ForeignKey(user,on_delete=models.CASCADE,null=True)

class album_like(models.Model):
    album_id = models.CharField(max_length=255,default='')
    user     = models.ForeignKey(user,on_delete=models.CASCADE,null=True)

class artist_like(models.Model):
    artist_id = models.CharField(max_length=255,default='')
    user      = models.ForeignKey(user,on_delete=models.CASCADE,null=True)


class music_rating(models.Model):
    user     = models.ManyToManyField(user)
    music_id = models.CharField(max_length=255,default='')
    rating   = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
        ,null=True
    ) 
class album_rating(models.Model):
    user      = models.ManyToManyField(user)
    album_id   = models.CharField(max_length=255,default='')
    rating    = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
        ,null=True
    )    
class artist_rating(models.Model):
    user      = models.ManyToManyField(user)
    artist_id   = models.CharField(max_length=255,default='')
    rating    = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
        ,null=True
    )        

class music_favorite(models.Model):
    user     = models.ManyToManyField(user)
    music_id = models.CharField(max_length=255,default='')

class album_favorite(models.Model):
    user     = models.ManyToManyField(user)
    album_id = models.CharField(max_length=255,default='')

class artist_favorite(models.Model):
    user      = models.ManyToManyField(user)
    artist_id = models.CharField(max_length=255,default='')     

class top_music_rating(models.Model):
    music_id = models.CharField(max_length=255,default='')
    rating = models.FloatField(
    validators=[MaxValueValidator(5), MinValueValidator(0)]
    ,null=True
    ) 
    vote_num = models.IntegerField(default=0)
class top_album_rating(models.Model):
    album_id = models.CharField(max_length=255,default='')
    rating = models.FloatField(
    validators=[MaxValueValidator(5), MinValueValidator(0)]
    ,null=True
    ) 
    vote_num = models.IntegerField(default=0)
    
class top_artist_rating(models.Model):
    artist_id = models.CharField(max_length=255,default='')
    vote_num = models.IntegerField(default=0)       
  