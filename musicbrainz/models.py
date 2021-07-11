from django.db import models

class genre(models.Model):
    name     = models.CharField(max_length=255,default='')
    genre_id = models.CharField(max_length=255,default='')
    description = models.CharField(max_length=99999,default='')