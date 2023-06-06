from rest_framework import serializers
from .models import Author, Games, Genres, Country, Publishers


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('__all__')


class GamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('__all__')


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = ('__all__')


class PublishersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publishers
        fields = ('__all__')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('__all__')
