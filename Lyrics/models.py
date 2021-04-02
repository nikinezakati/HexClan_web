from django.db import models
from User.models import user
from Page.models import Music

class lyrics(models.Model):
    music    = models.OneToOneField(Music,on_delete=models.CASCADE,null=True)
    context  = models.TextField()

class Liked_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    likes = models.OneToOneField(user,on_delete=models.CASCADE,null= True)
    lyric = models.ForeignKey(lyrics,on_delete=models.CASCADE,null=True)

class Commented_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    context = models.CharField(max_length=255,default='')
    user = models.OneToOneField(user,on_delete=models.CASCADE,null= True)
    lyric = models.ForeignKey(lyrics,on_delete=models.CASCADE,null=True)
