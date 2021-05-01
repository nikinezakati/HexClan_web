from rest_framework import serializers

from Page.models import page, Artist, Music, Album, URL
from musicbrainz.search_by_query import *


#class PageSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = page
#		fields = '__all__'

#class AlbumSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = Album
#		fields = '__all__'

#class ArtistSerializer(serializers.ModelSerializer):
#	albums = AlbumSerializer(many = True, read_only = True)
#	class Meta:
#		model = Artist
#		fields = '__all__'

#class MusicSerializer(serializers.ModelSerializer):
#	artists = ArtistSerializer(many = True, read_only = True)
#	music_album = AlbumSerializer(read_only = True)
#	class Meta:
#		model = Music
#		fields = '__all__'

#class URLSerializer(serializers.ModelSerializer):
#	class Meta:
#		model = URL
#		fields = '__all__'

class MusicSerializer(serializers.Serializer):
    class Nodes: 
        fields = (
        	'name',
        	'profile_type',
            'artists',
            'producer',
            'music_album',
            'genre',
            'release_date',
            'rating'
        )

class ArtistSerializer(serializers.Serializer):
    class Nodes: 
        fields = (
        	'name',
        	'profile_type',
            'artist_type',
            'begin_date',
            'end_date',
            'albums'
        )
        data = search_artist_by_name("Eminem")

class AlbumSerializer(serializers.Serializer):
    class Nodes: 
        fields = (
        	'name',
        	'profile_type',
            'release_date',
            'rating'
        )