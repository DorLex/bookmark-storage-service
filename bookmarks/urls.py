from django.urls import URLPattern, path

from bookmarks.api.bookmark import BookmarkViewSet

urlpatterns: list[URLPattern] = [
    path('', BookmarkViewSet.as_view({'post': 'create'}), name='bookmark-list'),
    path(
        '<int:bookmark_id>',
        BookmarkViewSet.as_view(
            {
                'get': 'retrieve',
                'delete': 'destroy',
            },
        ),
        name='bookmark-detail',
    ),
]
