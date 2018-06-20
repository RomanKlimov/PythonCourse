from django.forms import ModelForm

from wall.models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date']
