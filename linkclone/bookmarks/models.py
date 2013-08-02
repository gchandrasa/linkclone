import requests
import urlparse
from bs4 import BeautifulSoup

from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager


class Link(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField('URL', max_length=255)
    count = models.IntegerField(default=0, editable=False)
    latest_bookmarked = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-latest_bookmarked',)

    def __unicode__(self):
        return self.url

    @property
    def base_url(self):
        return urlparse.urlsplit(self.url)[1]

    def save(self, *args, **kwargs):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content)
        self.title = soup.find('title').text.strip()
        return super(Link, self).save(*args, **kwargs)


class Bookmark(models.Model):

    link = models.ForeignKey(Link, related_name='bookmarks')
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)

    tags = TaggableManager()

    class Meta:
        ordering = ('-date',)
        unique_together = ('link', 'user')

    def save(self, *args, **kwargs):
        bookmark = super(Bookmark, self).save(*args, **kwargs)
        self.link.count = self.link.bookmarks.count()
        self.link.save()
        return bookmark

