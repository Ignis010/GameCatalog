from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework
from catalog.models import Author, Games, Genres, Publishers, Country
from catalog.permission import IsAdminOrReadOnly
from catalog.serializers import AuthorSerializer, GamesSerializer, GenresSerializer, PublishersSerializer, \
    CountrySerializer
from catalog.service import AuthorFilters


# Create your views here.

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (rest_framework.DjangoFilterBackend,)
    filterset_class = AuthorFilters


class GamesViewSet(viewsets.ModelViewSet):
    queryset = Games.objects.all()
    serializer_class = GamesSerializer
    permission_classes = (IsAdminOrReadOnly,)


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly,)


class PublishersViewSet(viewsets.ModelViewSet):
    queryset = Publishers.objects.all()
    serializer_class = PublishersSerializer
    permission_classes = (IsAdminOrReadOnly,)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly)
