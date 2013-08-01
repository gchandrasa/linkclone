from django.conf.urls.defaults import *

urlpatterns = patterns('',

    url(r'^$', 'bookmarks.views.index'),
    url(r'^save$', 'bookmarks.views.save_bookmark', name='save_bookmark'),
    url(r'^login$', 'bookmarks.views.login', name='login_redirect'),
)

