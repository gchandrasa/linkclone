from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError

from haystack.query import SearchQuerySet

from .models import Link, Bookmark
from .forms import BookmarkForm


def index(request, template_name='bookmarks/index.html', context={}):
    form = BookmarkForm(request.POST or None)
    bookmarl_list = Bookmark.objects.all()[:10]
    context = {
        'bookmarl_list': bookmarl_list,
        'form': form,
    }

    return render(request, template_name, context)


def save_bookmark(request):

    url = request.POST.get('url', None)
    if url:
        link, is_created = Link.objects.get_or_create(url=url)
        try:
            bookmark = Bookmark.objects.create(link=link, user=request.user)
            tags = request.POST.get('tags', None)
            tags = [tag.strip() for tag in tags.split(",")]
            bookmark.tags.add(*tags)
            bookmark.save()
        except IntegrityError:
            messages.error(request, 'You already bookmark that URL')
        return redirect('bookmarks:index')
    return redirect('/')


def user_bookmark(request, username,
        template_name='bookmarks/user_bookmark.html', context={}):

    link_list = Link.objects.filter(bookmarks__user=request.user)
    context['link_list'] = link_list

    return render(request, template_name, context)


def search(request):
    q = request.GET.get('q', None)
    if q:
        results = SearchQuerySet().filter(content=q)
    else:
        results = None
    context = {
        'results': results,
        'q': q,
    }
    return render(request, 'bookmarks/results.html', context)
