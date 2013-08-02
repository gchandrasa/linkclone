from django.conf.urls import *

urlpatterns = patterns('linkclone.bookmarks.views',

    url(r'^$', 'index', name='index'),
    url(r'^save$', 'save_bookmark', name='save'),
    url(r'^login$', 'login', name='login_redirect'),
)
