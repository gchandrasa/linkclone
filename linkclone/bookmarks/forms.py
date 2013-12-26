from django import forms

from models import Link


class BookmarkForm(forms.Form):
    url = forms.CharField(widget=forms.TextInput(attrs={'placeholder':
        'Type or paste the URL to bookmark'}))


class LinkForm(forms.ModelForm):

    class Meta:
        model = Link
