from django.urls import path

from wall.views import wall, repost, PostCreateView, tag

urlpatterns = [
    path('id<int:user_id>/', wall, name='wall'),
    path('repost/<int:post_id>', repost, name='repost'),
    path('post/new', PostCreateView.as_view(), name='post'),
    path('tag/<str:tag>', tag, name='tag')
]
