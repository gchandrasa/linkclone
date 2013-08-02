from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import IntegrityError

from .models import Link, Bookmark


def index(request, template_name='bookmarks/index.html', context={}):

    link_list = Link.objects.all()[:10]
    context['link_list'] = link_list

    return render(request, template_name, context)


def save_bookmark(request):

    url = request.POST.get('url', None)
    if url:
        link, created = Link.objects.get_or_create(url=url)
        try:
            Bookmark.objects.create(link=link, user=request.user)
        except IntegrityError:
            messages.error(request, 'You already bookmark that URL')

    return redirect('/')


def user_bookmark(request, username,
        template_name='bookmarks/user_bookmark.html', context={}):

    link_list = Link.objects.filter(bookmarks__user=request.user)
    context['link_list'] = link_list

    return render(request, template_name, context)


def login(request):
    return redirect('/u/%s' % request.user)
