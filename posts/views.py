from urllib import request
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Post
from django import forms
from .forms import PostForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts = Post.objects.all().order_by('-created_at')[:20]
    # Show
    return render(request, 'posts.html',
                  {'posts' : posts})

def delete(request,  post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect('/')

def like(request, post_id):
    newlike=Post.objects.get(id=post_id)
    newlike.likecount += 1
    newlike.save()
    return HttpResponseRedirect('/')

def edit(request, post_id):
    posts=Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES,instance=posts)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    
    # Show
    return render(request, 'edit.html',
                  {'posts' : posts})