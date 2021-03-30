from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Page(models.Model):
    name        = models.CharField(max_length=100)
    profie_type = models.CharField(max_length=10,default='')
    class Meta:
        abstract = True

class Artist(Page):
    artist_type = models.CharField(max_length=100)
    begin_date  = models.DateField(auto_now=False, auto_now_add=False,null=True)
    end_date    = models.DateField(auto_now=False, auto_now_add=False , null= True)
    albums      = models.ManyToManyField('Music',related_name='+')
    likes       = models.ManyToManyField('User')        

class Music(Page):
    artist       = models.OneToOneField('Artist',on_delete=models.CASCADE)
    producer     = models.CharField(max_length=100)
    album        = models.OneToOneField('Album',on_delete=models.CASCADE,null=True)
    genre        = models.CharField(max_length=100)
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    rating       = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
        ,null=True
    )
    likes        = models.ManyToManyField('User')
    lyric        = models.OneToOneField('Lyric',on_delete=models.CASCADE,null=True)
    urls = models.ManyToManyField('URL')

class Album(Page):
    release_date = models.DateField(auto_now=False, auto_now_add=False)
    rating       = models.IntegerField(
        validators=[MaxValueValidator(100), MinValueValidator(1)]
        ,null=True
    )
    likes        = models.ManyToManyField('User')    

class Comment(models.Model):
    page_type = models.CharField(max_length=100)
    user      = models.OneToOneField('User',on_delete=models.CASCADE)
    context   = models.CharField(max_length=500)

class URL(models.Model):
    content = models.CharField(max_length=500)

class Lyric(models.Model):
    context       = models.TextField()
    liked_section = models.ManyToManyField('Liked_Section')
    commented = models.ManyToManyField('Commented_Section')

class Liked_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    likes = models.OneToOneField('User',on_delete=models.CASCADE)

class Commented_Section(models.Model):
    start_index = models.IntegerField()
    end_index = models.IntegerField()
    context = models.CharField(max_length=500)
    user = models.OneToOneField('User',on_delete=models.CASCADE)

class User(models.Model):
    first_name        = models.CharField(max_length=100)
    last_name         = models.CharField(max_length=100)
    email             = models.EmailField(max_length=254)
    password          = models.CharField(max_length=50)
    description       = models.CharField(max_length=500)
    avatar            = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)
    music_ratings     = models.ManyToManyField('Music')
    album_ratings     = models.ManyToManyField('Album',related_name='+')
    favorites_musics  = models.ManyToManyField('Music',related_name='+')
    favorites_albums  = models.ManyToManyField('Album')
    favorites_artists = models.ManyToManyField('Artist')


    