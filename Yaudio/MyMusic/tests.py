from django.contrib.auth.models import User
from django.test import TestCase, Client

from MyMusic.models import Artist, City, Country


class ArtistAdditionTest(TestCase):
    def setUp(self):
        User.objects.create_user(username="admin", password="admin")
        country = Country(name='USA').save()
        City(name='TORONTO', country=Country.objects.get(name='USA').id).save()

    def test_add_artitst_authorized(self):
        c = Client()
        c.login(username="admin", password="admin")
        resp = c.post("music/artists/new", {'username': 'admin',
                                    'password': 'admin'})
        print(resp.status_code)
        # resp = c.post('/artists/new', {'name': 'Three Days Grace',
        #                         'city': City.objects.filter(name='TORONTO'),
        #                         'year_start': 2003,
        #                         'year_end': 2018})
        # print(resp.status_code)
        # print(Artist.objects.all())
