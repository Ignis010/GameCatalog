from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'authors', views.AuthorViewSet)
router.register(r'games', views.GamesViewSet)
router.register(r'genres', views.GenresViewSet)
router.register(r'publishers', views.PublishersViewSet)
router.register(r'countries', views.CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/<ip>', include('rest_framework.urls', namespace='rest_framework'))
]
