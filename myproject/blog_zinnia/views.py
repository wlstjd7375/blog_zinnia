from django.shortcuts import render, redirect, get_object_or_404

from zinnia.models import Entry
from .models import MyUser

def index(request):
    entries = get_entries(5)
    return render(request, 'blog/index.html', {'entries': entries})

def entry_detail(request, pk, date, slug):
    entry = get_object_or_404(Entry, pk=pk)
    entries = get_entries(5)
    return render(request, 'blog/entry_detail_alternate.html', {'object': entry, 'entries': entries, 'date': date})

def author_detail(request, author):
    author = get_object_or_404(MyUser, username=author)
    username = author.username.__str__()
    name = author.name.__str__()
    email = author.email.__str__()
    url = author.url.__str__()
    intro = author.intro.__str__()
    if author.profile:
        profile = author.profile.url.__str__()
    else:
        profile = ''
    author = {'username': username, 'name': name, 'email': email, 'url': url, 'intro': intro, 'profile': profile}
    return render(request, 'blog/author_detail.html', {'author': author})


def get_entries(cnt):
    _entries = Entry.published.all()[:cnt]
    entries = []
    for _entry in _entries:
        date = get_date(_entry)
        entry = {'entry': _entry, 'date': date}
        entries.append(entry)
    return entries

def get_date(_entry):
    _date = _entry.publication_date
    year = _date.strftime('%Y')
    month = _date.strftime('%m')
    day = _date.strftime('%d')
    date = year+month+day
    return date
