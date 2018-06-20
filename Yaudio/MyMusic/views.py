from __future__ import unicode_literals

from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db.models import F
from django.forms import modelform_factory, PasswordInput
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, FormView, CreateView
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE

from MyMusic.forms import ArtistForm, login_form
from MyMusic.models import Artist, Playlist, Audio, Like


def do_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            if 'next' in request.GET:
                return HttpResponseRedirect(request.GET['next'])
            else:
                return HttpResponseRedirect(reverse('artists'))
        else:
            HttpResponseRedirect(reverse('login'))
        if user is not None:
            return HttpResponse("gg wp")
        else:
            return HttpResponse("loo$er")
    else:
        return render(request,
                      'login.html',
                      {'form': login_form})


@csrf_exempt
def like(request):
    track_id = request.POST['id']
    obj = Like.objects.get_or_create(user=request.user, audio=Audio.objects.get(pk=track_id))
    if obj[1]:
        return HttpResponse(status=201)
    else:
        obj[0].delete()
        return HttpResponse(status=200)


class HelloView(TemplateView):
    template_name = 'MyMusic/hello.html'


class ListTracksView(ListView):
    model = Audio
    context_object_name = 'tracks'


class ListArtistView(ListView):
    model = Artist
    context_object_name = 'artists'
    template_name = 'MyMusic/artist_list.html'


class AddNewArtistView(CreateView):
    template_name = 'MyMusic/add_new_artist.html'
    form_class = ArtistForm
    success_url = reverse_lazy('artists')

    def form_valid(self, form):
        self.object = form.save()
        # todo
        # Action(model_type='artist', user_id=something,
        #        object_id=self.object.id)
        return super().form_valid(form)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


@login_required
def add_new_artist(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            f = ArtistForm(data=request.POST)
            f.save()
            return HttpResponseRedirect(reverse('artists'))
        else:
            return render(request, 'MyMusic/add_new_artist.html', {'form': ArtistForm()})
    else:
        return HttpResponseRedirect(reverse('login'))


def artist_songs(request, id):
    artist = Artist.objects.get(id=id)
    songs = Audio.objects.filter(artist=artist)
    return render(request, 'MyMusic/artist_songs.html',
                  {'artist': artist,
                   'songs': songs})


def entities(request, entity):
    d = {'countries': 'Country',
         'audios': 'Audio',
         'artists': 'Artist',
         'cities': 'City',
         'playlists': 'Playlist',
         'likes': 'Like'}
    try:
        query = eval(d[entity] + '.objects.all()')
        return render(request, 'MyMusic/entities.html', {'entities': query})
    except:
        return render(request, 'MyMusic/entities.html', {'error': 'No such models'})


def query(request):
    # q = Country.objects.all()

    # q = Artist.objects.filter(year_start=1983, city_id=2)

    # all spb artists - var 1
    # c = City.objects.get(name="St.Petersburg")
    # q = Artist.objects.filter(city_id=c.id)

    # var 2
    # c = City.objects.get(name="St.Petersburg")
    # q = c.artist_set

    # var 3
    # q = Artist.objects.filter(city__name="Moscow")

    # artist that started after 1980
    # q = Artist.objects.raw(
    #    "select * from music_artist where year_start > 1980")

    # q = Artist.objects.filter(year_start__lt=1980)
    # q = q.exclude(city__name="Moscow")

    # q1 = Q(city__name="Moscow")
    # q2 = Q(year_start__lt=1980)

    # q3 = q1 & ~q2
    # q = Artist.objects.filter(q3)

    # lst = q.values()

    # q = Playlist.objects.get(pl_name="roma").audios.add
    # reverse
    # q = Audio.objects.get(id=2).playlist_set

    # period of work:
    # q = Artist.objects.filter(year_end__lt=20 + F("year_start"))

    # order

    # q = Artist.objects.order_by("-year_start")
    # lst = q.values()

    r = Audio.objects.all().values()

    return HttpResponse(r)
