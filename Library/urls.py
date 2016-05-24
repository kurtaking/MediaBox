from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^user_dashboard', views.user_dashboard, name='user_dashboard'),
    url(r'^libraries', views.libraries, name='libraries'),
    url(r'^vinyls', views.vinyls, name='vinyls'),
    url(r'^vinyl/(?P<id>\d+)/', views.vinyl_detail, name='vinyl_detail'),
    url(r'^by_artist', views.by_artist, name='by_artist'),
    url(r'^movies', views.movies, name='movies'),
    url(r'^video_games', views.video_games, name='video_games'),
    url(r'^books', views.books, name='books'),
    url(r'^settings', views.settings, name='settings'),
]




