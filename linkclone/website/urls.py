from django.conf.urls import *

urlpatterns = patterns('linkclone.website.views',

    url(r'^$', 'index', name='index'),
)
