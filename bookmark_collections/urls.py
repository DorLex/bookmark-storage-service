from django.urls import path

from bookmark_collections.views.bm_collection import CollectionAPIView
from bookmark_collections.views.bm_collections import CollectionsAPIView

urlpatterns = [
    path('', CollectionsAPIView.as_view(), name='collections'),
    path('<int:collection_id>', CollectionAPIView.as_view()),
]
