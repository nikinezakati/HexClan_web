from django.db import models
from User.models import user
import datetime
from django.utils import timezone

class lyrics(models.Model):
    music_id =  models.CharField(max_length=255,default='')
    context  = models.JSONField()

class Liked_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    likes = models.ManyToManyField(user)
    lyric = models.ForeignKey(lyrics,on_delete=models.CASCADE,null=True)

class Commented_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    context = models.CharField(max_length=255,default='')
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    lyric = models.ForeignKey(lyrics,on_delete=models.CASCADE,null=True)
    date  = models.DateTimeField(blank=True, null=True ,default=timezone.now)