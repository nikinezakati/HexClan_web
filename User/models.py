from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator

class user(AbstractUser):
    description       = models.CharField(max_length=255, default='', null = True, blank = True)
    avatar            = models.ImageField(upload_to='Images/', height_field=None, width_field=None, max_length=100, null = True, blank = True)
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



class music_rating(models.Model):
    user     = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    music_id = models.CharField(max_length=255,default='')
    rating   = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
        ,null=True
    ) 
class album_rating(models.Model):
    user      = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    album_id   = models.CharField(max_length=255,default='')
    rating    = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)]
        ,null=True
    )    


class music_favorite(models.Model):
    user     = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    music_id = models.CharField(max_length=255,default='')

class album_favorite(models.Model):
    user     = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    album_id = models.CharField(max_length=255,default='')

class artist_favorite(models.Model):
    user      = models.ForeignKey(user,on_delete=models.CASCADE,null=True)
    artist_id = models.CharField(max_length=255,default='')     


class total_music_rating(models.Model):
    music_id = models.CharField(max_length=255,default='')
    rating = models.FloatField(
    validators=[MaxValueValidator(5), MinValueValidator(0)]
    ,null=True
    ) 
    vote_num = models.IntegerField(default=0)

class total_album_rating(models.Model):
    album_id = models.CharField(max_length=255,default='')
    rating = models.FloatField(
    validators=[MaxValueValidator(5), MinValueValidator(0)]
    ,null=True
    ) 
    vote_num = models.IntegerField(default=0)
    
class total_artist_followings(models.Model):
    artist_id     = models.CharField(max_length=255,default='')
    following_num = models.IntegerField(default=0)       
  