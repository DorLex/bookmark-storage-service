from django.contrib import admin

from bookmarks.models import Bookmark


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('pk', '__str__', 'user')
    filter_horizontal = ('collections',)
    readonly_fields = ('created_at', 'updated_at')
