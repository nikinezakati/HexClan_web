from django.db import models
from User.models import user


class lyrics(models.Model):
    music_id =  models.CharField(max_length=255,default='')
    context  = models.TextField()

class Liked_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    likes = models.ManyToManyField(user)
    lyric = models.ForeignKey(lyrics,on_delete=models.CASCADE,null=True)

class Commented_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    context = models.CharField(max_length=255,default='')
    user = models.ManyToManyField(user)
    lyric = models.ForeignKey(lyrics,on_delete=models.CASCADE,null=True)
