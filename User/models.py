from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
import datetime
from django.utils import timezone

class user(AbstractUser):
    description = models.CharField(
        max_length=255, default='', null=True, blank=True)
    avatar = models.ImageField(upload_to='Images/', height_field=None, default='/Images/default.jpg',
     width_field=None, max_length=100, null=True, blank=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', ]

    def __str__(self):
        return self.username

    def get_favorite_artists(self):
        result = []
        query = artist_favorite.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append(l.artist_id)
        return result

    def get_favorite_albums(self):
        result = []
        query = album_favorite.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append(l.album_id)
        return result

    def get_favorite_musics(self):
        result = []
        query = music_favorite.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append(l.music_id)
        return result

    def get_rating_musics(self):
        result = []
        query = music_rating.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append((l.music_id, l.rating))
        return result

    def get_rating_albums(self):
        result = []
        query = album_rating.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append((l.album_id, l.rating))
        return result

    def get_comment_artists(self):
        result = []
        query = artist_comment.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append((l.artist_id, l.context))
        return result

    def get_comment_musics(self):
        result = []
        query = music_comment.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append((l.music_id, l.context))
        return result

    def get_comment_albums(self):
        result = []
        query = album_comment.objects.all().filter(user=self)
        if len(query) != 0:
            for l in query:
                if l.user == self:
                    result.append((l.album_id, l.context))
        return result


class music_comment(models.Model):
    music_id = models.CharField(max_length=255, default='')
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    context = models.CharField(max_length=5000, default='')
    date      = models.DateTimeField(blank=True, null=True ,default=timezone.now)


class album_comment(models.Model):
    album_id = models.CharField(max_length=255, default='')
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    context = models.CharField(max_length=5000, default='')
    date      = models.DateTimeField(blank=True, null=True ,default=timezone.now)


class artist_comment(models.Model):
    artist_id = models.CharField(max_length=255, default='')
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    context = models.CharField(max_length=5000, default='')
    date      = models.DateTimeField(blank=True, null=True ,default=timezone.now)


class music_rating(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    music_id = models.CharField(max_length=255, default='')
    rating = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], null=True
    )


class album_rating(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    album_id = models.CharField(max_length=255, default='')
    rating = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], null=True
    )


class music_favorite(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    music_id = models.CharField(max_length=255, default='')


class album_favorite(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    album_id = models.CharField(max_length=255, default='')


class artist_favorite(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True)
    artist_id = models.CharField(max_length=255, default='')


class total_music_rating(models.Model):
    music_id = models.CharField(max_length=255, default='')
    rating = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], null=True
    )
    vote_num = models.IntegerField(default=0)
    artist_id = models.CharField(max_length=255,default='')

class total_album_rating(models.Model):
    album_id = models.CharField(max_length=255, default='')
    rating = models.FloatField(
        validators=[MaxValueValidator(5), MinValueValidator(0)], null=True
    )
    vote_num = models.IntegerField(default=0)
    artist_id = models.CharField(max_length=255,default='')


class total_artist_followings(models.Model):
    artist_id = models.CharField(max_length=255, default='')
    following_num = models.IntegerField(default=0)
