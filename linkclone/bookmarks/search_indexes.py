from haystack import indexes

from .models import Bookmark


class BookmarkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')
    title = indexes.CharField()
    url = indexes.CharField()

    def get_model(self):
        return Bookmark

    def prepare_user(self, obj):
        return obj.user.username

    def prepare_title(self, obj):
        return obj.link.title

    def prepare_url(self, obj):
        return obj.link.url
