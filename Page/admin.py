from django.contrib import admin

# Register your models here.
from Page.models import page, Artist, Music, Album, URL


class PageAdmin(admin.ModelAdmin):
    fields = ['name', 'profile_type']

admin.site.register(page, PageAdmin)

class ArtistAdmin(admin.ModelAdmin):
    fields = ['name', 'profile_type', 'artist_type', 'begin_date', 'end_date', 'albums']
    
admin.site.register(Artist, ArtistAdmin)

class MusicAdmin(admin.ModelAdmin):
    fields = ['name', 'profile_type', 'artists', 'producer', 'music_album', 'genre', 'release_date', 'rating']
    
admin.site.register(Music, MusicAdmin)

class AlbumAdmin(admin.ModelAdmin):
    fields = ['name', 'profile_type', 'release_date', 'rating']
    
admin.site.register(Album, AlbumAdmin)

class URLAdmin(admin.ModelAdmin):
    fields = ['name', 'content', 'music']
    
admin.site.register(URL, URLAdmin)