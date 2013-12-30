from django.contrib import admin

from .models import Link, Bookmark


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('user', 'link', 'date')


class LinkAdmin(admin.ModelAdmin):
    list_display = ('url', 'count')


admin.site.register(Bookmark, BookmarkAdmin)
admin.site.register(Link, LinkAdmin)
