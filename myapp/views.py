from django.shortcuts import render
from django.utils import timezone
from .models import Post, Note


def home(request):
    return render(request, 'myapp/home.html',{})


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'myapp/post_list.html',{'posts':posts})


def note_list(request):
    notes = Note.objects.all()
    return render(request, 'myapp/note_list.html',{'notes':notes})