from haystack import indexes

from .models import Bookmark


class BookmarkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    user = indexes.CharField(model_attr='user')

    def get_model(self):
        return Bookmark

    def prepare_user(self, obj):
        return obj.user.username
