from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Genres(models.Model):
    genre_name = models.CharField(verbose_name="Наименование", max_length=100)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Publishers(models.Model):
    publishers_name = models.CharField(verbose_name="Наименование", max_length=100)
    date_registration = models.DateField(verbose_name="Дата регистрации", auto_now_add=True)
    number = models.IntegerField(verbose_name="Номер телефона", blank=True)
    site = models.URLField(verbose_name="Официальный сайт", max_length=250)

    def __str__(self):
        return self.publishers_name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Author(models.Model):
    surname = models.CharField(verbose_name="Фамилия", max_length=200)
    name = models.CharField(verbose_name="Имя", max_length=150)
    patronymic = models.CharField(verbose_name="Отчество", max_length=200, blank=True)
    author_describe = models.TextField(verbose_name="Описание автора", blank=True)
    birthday = models.IntegerField(verbose_name="Год рождения", )

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Country(models.Model):
    country_name = models.CharField(verbose_name="Название", max_length=200)

    def __str__(self):
        return self.country_name

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Games(models.Model):
    game_name = models.CharField(verbose_name="Название", max_length=100)
    genre = models.ForeignKey(Genres, verbose_name="Жанр", on_delete=models.PROTECT)
    publisher = models.ForeignKey(Publishers, verbose_name="Издатель", on_delete=models.PROTECT)
    photo = models.ImageField(verbose_name="Изображение", upload_to='gameimg/%Y/%m/%d')
    game_describe = models.TextField(verbose_name="Описание игры", blank=True)
    date_publication = models.DateTimeField(verbose_name="Дата публикации на сайте", auto_now_add=True)
    author = models.ForeignKey(Author, verbose_name="Автор", on_delete=models.CASCADE)
    country = models.ForeignKey(Country, verbose_name="Страна производитель", on_delete=models.CASCADE)
    environment = models.CharField(verbose_name="Сеттинг", max_length=100)
    editor = models.ForeignKey(User, verbose_name='Редактор', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.game_name

    class Meta:
        verbose_name = 'Игра'
        verbose_name_plural = 'Игры'
