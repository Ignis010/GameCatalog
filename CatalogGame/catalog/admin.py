from django.contrib import admin
from catalog.models import Genres, Publishers, Country, Author, Games

# Register your models here.
admin.site.register(Genres)
admin.site.register(Publishers)
admin.site.register(Country)
admin.site.register(Author)
admin.site.register(Games)
