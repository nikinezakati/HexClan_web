from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator



# class page(models.Model):
#     name        = models.CharField(max_length=255,default='')
#     profile_type = models.CharField(max_length=255,default='')
    
# class Artist(page):
#     artist_type = models.CharField(max_length=255,default='')
#     begin_date  = models.DateField(auto_now=False, auto_now_add=False,null=True)
#     end_date    = models.DateField(auto_now=False, auto_now_add=False ,null= True)
# #    albums      = models.ManyToManyField('Album')
     
# class Music(page):
#     artists      = models.ManyToManyField('Artist')
#     #producer     = models.CharField(max_length=255,default='')
#     music_album  = models.ForeignKey('Album',on_delete=models.CASCADE,null=True)
#     #genre        = models.CharField(max_length=255,default='')
#     release_date = models.DateField(auto_now=False, auto_now_add=False,null= True)
#     rating       = models.FloatField(
#         validators=[MaxValueValidator(5), MinValueValidator(0)]
#         ,null=True
#     )
    
# class Album(page):
#     release_date = models.DateField(auto_now=False, auto_now_add=False,null=True)
#     rating       = models.IntegerField(
#         validators=[MaxValueValidator(5), MinValueValidator(0)]
#         ,null=True,default=0
#     )
    
# class URL(models.Model):
#     name    = models.CharField(max_length=255,default='')
#     content = models.CharField(max_length=255,default='')
#     music   = models.ForeignKey(Music,on_delete=models.CASCADE,null=True)

