from django.contrib import admin
from django.conf import settings

from bookmarks.models import Link, Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user',)


class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'count')


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Link, LinkAdmin)

