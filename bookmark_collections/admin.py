from django.contrib import admin

from bookmark_collections.models import Collection


@admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
