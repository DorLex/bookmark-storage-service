from django.urls import URLPattern, path

from bookmarks.views.bookmark import BookmarkViewSet

urlpatterns: list[URLPattern] = [
    # path('', BookmarksAPIView.as_view(), name='bookmarks'),
    # path('<int:bookmark_id>', BookmarkAPIView.as_view(), name='bookmark'),
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
