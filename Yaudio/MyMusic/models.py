from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Audio(models.Model):
    title = models.CharField(max_length=20)
    artist = models.ForeignKey("Artist", related_name="audios", on_delete=models.PROTECT)
    year = models.PositiveSmallIntegerField()
    duration = models.DurationField()
    liked = models.ManyToManyField(User, through="Like", related_name="liked")

    def __str__(self):
        return self.artist.name + ' - ' + self.title + ' (likes:%d)' % self.liked.count()


class Artist(models.Model):
    name = models.CharField(max_length=70)
    city = models.ForeignKey("City", on_delete=models.PROTECT)
    year_start = models.PositiveSmallIntegerField()
    year_end = models.PositiveSmallIntegerField(null=True)
    photo = models.ImageField(upload_to='artists_photo/', null=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=30)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    def __str__(self):
        return self.name + ' - ' + self.country.name


class Playlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="playlists")
    name = models.CharField(max_length=30)
    audios = models.ManyToManyField(Audio)

    # liked = models.ManyToManyField(User, through="Like", related_name="liked")

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    audio = models.ForeignKey(Audio, on_delete=models.CASCADE, null=True)
    when = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + " liked " + self.audio.title
