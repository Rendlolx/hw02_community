from django.shortcuts import get_object_or_404, get_list_or_404, render, redirect
from django.core.paginator import Paginator
from .models import Group, Post, User
from .forms import PostForm
from django.contrib.auth.decorators import login_required


def index(request):
    template_main = 'posts/index.html'
    posts = Post.objects.all()
    #Показывать по 10 записей на странице
    page = Paginator(posts, 10)
    #Из URL извлекаем номер запрошенной страницы
    page_number = request.GET.get('page')
    #Получаем набор записей для страрницы с запрошенным номером
    page_obj = page.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template_main, context)


def group_posts(request, slug):
    template_group = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    page = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, template_group, context)


def profile(request, username):
    template_name = 'posts/profile.html'
    profile = get_list_or_404(Post, author__username=username)
    author = get_object_or_404(User, username=username)
    page = Paginator(profile, 10)
    page_number = request.GET.get('page')
    page_obj = page.get_page(page_number)
    post_count = Post.objects.filter(author__username=username).count()
    context ={
        'page_obj': page_obj,
        'post_count': post_count,
        'author': author
    }
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    post_count = Post.objects.filter(author=post_id).all().count()
    context = {
        'post': post,
        'post_count': post_count
    }
    return render(request, template_name, context)


@login_required
def post_create(request):
    template_name = 'posts/create_post.html'
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=post.author.username)
    context = {
        'form': form
    }
    return render(request, template_name, context)


@login_required
def post_edit(request):
    template_name = 'posts/create_post.html'
    form = PostForm(request.POST)
    if form.is_valid():
        post = form.save(commit=False)
        post.author = request.user
        post.save()
        return redirect('posts:profile', username=request.user)
    context = {
        'form': form
    }
    return render(request, template_name, context)