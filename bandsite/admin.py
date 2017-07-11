from django.contrib import admin

# Register your models here.
from .models import Media, Music, Video, Photo

admin.site.register(Music)
admin.site.register(Video)
admin.site.register(Photo)