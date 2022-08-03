from django.shortcuts import get_object_or_404, get_list_or_404, render

from django.core.paginator import Paginator

from .models import Group, Post, User


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
    context = {
        'post': post
    }
    return render(request, template_name, context)
