from __future__ import unicode_literals

from django.db import models


class Media(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    description = models.TextField(max_length=1000)
    source = models.CharField(max_length=200)
    type = None

    class Meta:
        abstract = True


class Music(Media):
    type = "music"
    album_art_source = models.CharField(max_length=200)


class Video(Media):
    type = "video"


class Photo(Media):
    type = "photo"

