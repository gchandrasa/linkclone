from django import forms

from models import Link


class BookmarkForm(forms.Form):
    url = forms.CharField()


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
