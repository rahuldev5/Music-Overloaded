from django.contrib.auth.models import Permission, User
from django.db import models

class Album(models.Model):

    user = models.ForeignKey(User, default=1)
    album_title = models.CharField(max_length=500)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title


class Song(models.Model):

    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
