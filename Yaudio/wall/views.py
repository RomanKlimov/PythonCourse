from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from wall.forms import PostForm
from wall.models import Post, Repost


def wall(request, user_id):
    posts = Post.objects.filter(user_id=user_id).order_by("-date")
    return render(request, "wall/wall.html", {"posts": posts})


def repost(request, post_id):
    if request.method == 'POST':
        new = Post()
        origin = Post.objects.get(id=post_id)
        new.user_id = request.user.id
        new.text = 'RT "%s"' % origin.text
        new.save()
        repost = Repost()
        repost.text = new.text
        repost.source_id = post_id
        repost.destination_id = new.id
        repost.save()
        return HttpResponseRedirect(reverse("wall", args=(request.user.id,)))


class PostCreateView(CreateView):
    template_name = 'wall/add_post.html'
    form_class = PostForm
    success_url = reverse_lazy('post')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return HttpResponseRedirect(self.get_success_url())


def tag(request, tag):
    posts = Post.objects.filter(text__contains='#' + tag)
    return render(request, "wall/tag_posts.html",
                  {"posts": posts,
                   "tag":tag})
