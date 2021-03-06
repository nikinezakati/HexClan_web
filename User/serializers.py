from rest_framework import serializers
from .models import user
from django.forms.fields import CharField
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
User = get_user_model()


class UpdateUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(validators=[UniqueValidator(queryset=User.objects.all())])
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'description')

    def update(self, instance, validated_data):
        instance.username = validated_data['username']
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.description = validated_data['description']
        instance.save()

        return instance

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'avatar', 'description')


class UpdateAvatarUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('avatar',)
    def update(self, instance, validated_data):
        instance.avatar = validated_data['avatar']
        instance.save()
        return instance
     

    
