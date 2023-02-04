from django.shortcuts import render, get_object_or_404
from theList.models import Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def myList(request):
    auth = request.user.is_authenticated
    context = {
        'userLoggedIn': auth
    }
    if auth:
        entries = Entry.objects.filter(user__exact=request.user)
        context['entries'] = entries
        context['username'] = request.user.username
        context['password'] = request.user.password
    try:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request, user)
        return HttpResponseRedirect(reverse('index'))
    except:
        return render(request, 'theList/index.html', context)
    
def logoutView(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def detail(request, entry_id):
    entry = get_object_or_404(Entry, pk=entry_id)
    try:
        entry.entryText = request.POST['entryText']
        entry.title = request.POST['title']
        entry.save()
        return HttpResponseRedirect(reverse('index'))
    except:
        context = {'entry': entry}
        return render(request, 'theList/detail.html', context)

def creation(request):
    entry = Entry(title="Title", entryText="Entry Text", user=request.user)
    try:
        entry.entryText = request.POST['entryText']
        entry.title = request.POST['title']
        entry.save()
        return HttpResponseRedirect(reverse('index'))
    except:
        context = {'entry': entry}
        return render(request, 'theList/creation.html', context)


def accountCreation(request):
    try:
        user = User.objects.create_user(
            username=request.POST['username'],
            password=request.POST['password'],
            email=request.POST['email'],
            first_name=request.POST['firstName'],
            last_name=request.POST['lastName']
        )
        user.save()
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    except:
        context = {
            'username': '',
            'password': '',
        }
        return render(request, 'theList/accountCreation.html', context)

def deleteEntryView(request, entry_id):
    Entry.objects.get(id__exact=entry_id).delete()
    return HttpResponseRedirect(reverse('index'))