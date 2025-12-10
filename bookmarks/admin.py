from django.contrib import admin

from bookmarks.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    filter_horizontal = ('collections',)
    readonly_fields = ('created_at', 'updated_at')
