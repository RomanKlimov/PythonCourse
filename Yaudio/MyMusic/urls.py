from django.urls import path

from MyMusic.views import *

urlpatterns = [
    path('tracks/', ListTracksView.as_view()),
    path('artist/<int:id>/', artist_songs, name='artist_songs'),
    # path('<str:entity>/', entities, name='entities'),
    path('query/', query, name='query'),
    path('artists/new', AddNewArtistView.as_view(), name='add_new_artist'),
    path('artists/', ListArtistView.as_view(), name='artists'),
    path('', HelloView.as_view()),
    path('tracks/like', like, name='like')
]
