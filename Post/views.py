import os

from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,reverse
from .forms import PostForm
from django.contrib import messages
# Create your views here.
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
def index(request):
    context=dict()
    context['posts']=Post.objects.all()

    return render(request,"index.html",context)
def about(request):
    return render(request,"about.html")
@login_required(login_url="user:login")
def dashboard(request):
    posts=Post.objects.filter(author=request.user)
    context={
        "posts":posts
    }
    return render(request,"dashboard.html",context)
@login_required(login_url="user:login")
def addpost(request):
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        post=form.save(commit=False)
        post.author=request.user
        post.save()
        messages.success(request,"Post Oluşturuldu")
        return redirect("post:dashboard")
    return render(request,"addpost.html",{"form":form})
def detail(request,id):
    post = get_object_or_404(Post,id=id)
    comments=post.comments.all()
    context={
        "post":post,
        "comments":comments,
    }
    return  render(request,"detail.html",context)
@login_required(login_url="user:login")
def updatePost(request,id):
    post = get_object_or_404(Post,id=id)
    form=PostForm(request.POST or None, request.FILES or None,instance=post)
    if form.is_valid():
        post = form.save(commit=False)
        post.author=request.user
        post.save()
        messages.success(request,"Post güncellendi.")
        return redirect("post:dashboard")
    return render(request,"update.html",{"form":form})
@login_required(login_url="user:login")
def deletePost(request,id):
    post = get_object_or_404(Post,id=id)
    post.delete()
    messages.success(request,"Post silindi.")
    return redirect("post:dashboard")
def addComment(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method == "POST":
        comment_author=request.POST.get("comment_author")
        comment_content=request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.post=post
        newComment.save()
    return redirect(reverse("post:detail",kwargs={"id":id}))


