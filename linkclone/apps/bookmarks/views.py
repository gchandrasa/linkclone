from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.context import RequestContext
from django.contrib import messages
from django.db import IntegrityError

from bookmarks.models import Link, Bookmark

def index(request, template_name='bookmarks/index.html', context={}):

    link_list = Link.objects.all()[:10]
    context['link_list'] = link_list

    return render_to_response(template_name, context, RequestContext(request))


def save_bookmark(request):

    url = request.POST.get('url', None)
    if url:
        link, created = Link.objects.get_or_create(url=url)
        try:
            bookmark = Bookmark.objects.create(link=link, user=request.user)
        except IntegrityError:
            messages.error(request, 'You already bookmark that URL')

    return HttpResponseRedirect('/')


def user_bookmark(request, username,
    template_name='bookmarks/user_bookmark.html', context={}):

    link_list = Link.objects.filter(bookmarks__user=request.user)
    context['link_list'] = link_list

    return render_to_response(template_name, context, RequestContext(request))


def login(request):
    return HttpResponseRedirect('/u/%s' % request.user)

