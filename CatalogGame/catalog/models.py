from django.db import models


# Create your models here.


class Games(models.Model):
    game_name = models.CharField(varbse_name="Game name", max_length=100)
    genre = models.ForeignKey(Genres, verbose_name="Genre", on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publishers, verbose_name="Publisher", on_delete=models.PROTECT)
    photo = models.ImageField(verbose_name="Photo", upload_to='gameimg/%Y/%m/%d')
    game_describe = models.TextField(verbose_name="Game describe", blank=True)
    date_publication = models.DateTimeField(verbose_name="Date publication", auto_now_add=True)
    author = models.ForeignKey(Author, verbose_name="Author", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, verbose_name="Country", on_delete=models.CASCADE)
    environment = models.CharField(verbose_name="Environment", max_length=100)

    def __str__(self):
        return f'{self.game_name}, {self.publisher},{self.author},{self.date_publication}'

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'


class Publishers(models.Model):
    publishers_name = models.CharField(verbose_name="Publishers name", max_length=100)
    date_registration = models.DateTimeField(verbose_name="Date registration", auto_now_add=True)
    number = models.IntegerField(verbose_name="Number", max_length=16)
    site = models.CharField(verbose_name="Site", max_length=250)

    def __str__(self):
        return f'{self.publishers_name},{self.date_registration}'

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Genres(models.Model):
    genre_name = models.CharField(verbose_name="Genre name", max_length=100)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Author(models.Model):
    surname = models.CharField(verbose_name="Surname", max_length=200)
    name = models.CharField(verbose_name="Name", max_length=150)
    patronymic = models.CharField(verbose_name="Patronymic", max_length=200)
    author_describe = models.TextField(verbose_name="Author describe", blank=True)
    birthday = models.DateTimeField(verbose_name="Birthday")

    def __str__(self):
        return f'{self.surname}, {self.name}'

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Country(models.Model):
    country_name = models.CharField(verbose_name="Country name", max_length=200)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'
