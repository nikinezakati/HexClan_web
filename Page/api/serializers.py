from rest_framework import serializers

from Page.models import page, Artist, Music, Album, URL


class PageSerializer(serializers.ModelSerializer):
	class Meta:
		model = page
		fields = '__all__'

class AlbumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Album
		fields = '__all__'

class ArtistSerializer(serializers.ModelSerializer):
	albums = AlbumSerializer(many = True, read_only = True)
	class Meta:
		model = Artist
		fields = '__all__'

class MusicSerializer(serializers.ModelSerializer):
	artists = ArtistSerializer(many = True, read_only = True)
	music_album = AlbumSerializer(read_only = True)
	class Meta:
		model = Music
		fields = '__all__'

class URLSerializer(serializers.ModelSerializer):
	class Meta:
		model = URL
		fields = '__all__'

