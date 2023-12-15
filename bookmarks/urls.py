from django.urls import path

from .views import BookmarkAPIView

urlpatterns = [
    path('', BookmarkAPIView.as_view()),
]
