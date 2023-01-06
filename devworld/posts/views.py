from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Post, Rating,Comment
from .forms import PostForm, CommentForm, RatingForm


from django.contrib import messages
from .utils import *
#  from django.core.paginator import Paginator

# Create your views here.

def posts(request):
    posts, search_query = searchPosts(request)
    custom_range, posts = paginationPosts(request, posts, 6)

    context = {'posts': posts, 'search_query': search_query,'custom_range' : custom_range}
    return render(request, 'posts/posts.html', context )


def viewPost(request, pk):

    post = Post.objects.get(id=pk)
    comments = Comment.objects.all()

    comment_form = CommentForm()
    voting_form = RatingForm()

    if request.method == "POST" and 'comment' in request.POST:
        comment_form = CommentForm(request.POST, request.FILES)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.commenter = request.user.profile
            comment.post = post
            comment_form.save()

            post.getVoteCount
            messages.success(request,"Comment made")
        return redirect('single-post',pk=post.id)

    elif request.method =="POST" and 'up' in request.POST:
        voting_form = RatingForm(request.POST, request.FILES)
        if voting_form.is_valid():
            rating = voting_form.save(commit=False)
            rating.owner = request.user.profile
            rating.post = post
            rating.save()

            post.getVoteCount
            messages.success(request,"Rating submitted")
        return redirect('single-post', pk=post.id)


    context = {'comment_form':comment_form,'comments':comments, 'voting_form':voting_form,'post':post}
    return render(request, 'posts/post.html', context)


@login_required(login_url="login")
def addPost(request):
    current_profile = request.user.profile
    form = PostForm()
    template_name = 'posts/add_post.html'

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.owner = current_profile
            post.save()
            messages.success(request,"Post uploaded")
            return redirect('posts')

    context = {'form':form}
    return render(request,template_name,context)


@login_required(login_url="login")
def editPost(request, pk):
    profile = request.user.profile
    post = profile.post_set.get(id=pk)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,"Post updated")
            return redirect('account')

    context = {'form':form, 'profile':profile}
    return render(request, "posts/edit_post.html", context)


@login_required(login_url="login")
def deletePost(request,pk):
    profile = request.user.profile
    post = profile.post_set.get(id=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request,"Post deleted")
        return redirect('account')

    context = {'post':post, 'profile': profile}
    return render(request, "posts/delete_post.html", context)
