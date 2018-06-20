from django import template
from django.urls import reverse_lazy, reverse

register = template.Library()


@register.filter
def hashtag(value):
    replaced = []
    words = [word for word in value.split(' ')]
    for i in words:
        if i[0] == '#':
            replaced.append('<a href=\"' +
                            reverse('tag', kwargs={'tag': i[1:]}) +
                            '\">' + i + '</a>')
        else:
            replaced.append(i)
    return ' '.join(replaced)
