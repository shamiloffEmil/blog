from statistics import median

from django.contrib import auth, messages
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.shortcuts import render, get_object_or_404, render_to_response, get_list_or_404
from django.template.context_processors import csrf
from django.utils import timezone
from .forms import PostForm, DscForm, LikeForm, UserForm , ProfileForm  ,CommentForm
from .models import Post, Dsc, Like, Profile ,Comment
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)
    #averageLike = get_list_or_404(Like, post=post)#_list_or_404

    #averageLike2 =Like.objects.all().filter(post=post)

    #print(averageLike2)

    #average = 0;
    #for LikeScale in averageLike:
    #    average +=LikeScale.like

    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
        return render(request, 'blog/post_detail.html', {'post': post})
    else:
         form = PostForm()
         return render(request, 'blog/post_edit.html', {'form': form})

@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('blog.views.post_list')

@login_required
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()

        return render(request, 'blog/post_detail.html', {'post': post})

    else:
        form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})


# def about_list(request, pk):
#     post = get_object_or_404(Dsc, pk=pk)
#     return render(request, 'blog/about_list.html', {'post': post})

def add_like_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            like = form.save(commit=False)
            like.post = post
            like.save()
        # return redirect('blog.views.post_detail', pk=post.pk)   #blog/post_edit.html
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

    else:
        form = LikeForm()
        return render(request, 'blog/add_like_to_post.html', {'form': form})

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(request.user.id)
    print('///////')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post

            comment.save()

        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

    else:
        form = CommentForm()
        return render(request, 'blog/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('blog.views.post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('blog.views.post_detail', pk=post_pk)


def about_list(request, pk):
    user = get_object_or_404(User, pk=pk)
    return render(request, 'blog/about_list.html', {'user': user})


@login_required
def about_new(request, pk):
    user = get_object_or_404(User, pk=pk)
    prof = get_object_or_404(Profile, pk=user.profile.pk)
    form = ProfileForm(request.POST, instance=prof)

    if request.method == "POST":

        if form.is_valid():
            user = form.save(commit=False)
            user.save()

        return render(request, 'blog/about_list.html', {'user': user.user})

    else:
        form = ProfileForm(instance=prof)
        return render(request, 'blog/about_edit.html', {'form': form})



# @login_required
# @transaction.atomic
# def update_profile(request,pk):
#     if request.method == 'POST':
#         user_form = UserForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, ('Ваш профиль был успешно обновлен!'))
#             return redirect('settings:profile')
#         else:
#             messages.error(request, ('Пожалуйста, исправьте ошибки.'))
#     else:
#         user_form = UserForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profiles/profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })

