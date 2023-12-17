from django.urls import path

from bookmarks.views.bookmark import BookmarkAPIView
from bookmarks.views.bookmarks import BookmarksAPIView

urlpatterns = [
    path('', BookmarksAPIView.as_view()),
    path('<int:bookmark_id>', BookmarkAPIView.as_view()),
]
