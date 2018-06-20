from django.contrib import admin
from MyMusic.models import *

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Artist)
admin.site.register(Audio)
admin.site.register(Like)
admin.site.register(Playlist)