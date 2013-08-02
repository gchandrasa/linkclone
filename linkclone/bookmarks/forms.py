from django import forms

from models import Bookmark, Link


class BookmarkForm(forms.ModelForm):

    class Meta:
        model = Bookmark


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
