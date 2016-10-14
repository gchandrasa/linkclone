from django.conf.urls import include, url
from django.conf import settings
from django.contrib import admin
from linkclone.apps.bookmarks.views import search
admin.autodiscover()


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmarks/', include('linkclone.apps.bookmarks.urls',
        namespace='bookmarks')),
    url(r'^', include('linkclone.website.urls',
        namespace='website')),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^accounts/', include('linkclone.website.auth_urls')),
    url(r'^search/$', search, name='search'),
]

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            }),
    ]
