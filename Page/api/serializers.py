from rest_framework import serializers
from musicbrainz.search_by_query import *
from User.models import *

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

class ArtistCommentSerializer(serializers.Serializer):
    class Nodes: 
        model = artist_comment
        fields = ('context',)

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

class AlbumSerializer(serializers.Serializer):
    class Nodes: 
        fields = (
        	'name',
        	'profile_type',
            'release_date',
            'rating'
        )