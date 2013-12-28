from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmarks/', include('linkclone.bookmarks.urls',
        namespace='bookmarks')),
    url(r'^', include('linkclone.website.urls',
        namespace='website')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^search/$', 'linkclone.bookmarks.views.search', name='search'),
)


from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
            }),
    )
