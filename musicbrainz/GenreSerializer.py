from rest_framework import serializers
from musicbrainz.models import genre

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = genre
        fields = ['name']
