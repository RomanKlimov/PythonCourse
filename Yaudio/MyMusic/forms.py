from django.contrib.auth.models import User
from django.forms import ModelForm, IntegerField, modelform_factory, PasswordInput
from MyMusic.models import Artist


class ArtistForm(ModelForm):
    year_end = IntegerField(required=False)

    class Meta:
        model = Artist
        exclude = []


login_form = modelform_factory(model=User,
                               fields=['username', 'password'],
                               widgets={'password': PasswordInput()})
