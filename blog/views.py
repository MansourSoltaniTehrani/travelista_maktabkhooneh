from django.shortcuts import render
from django.shortcuts import get_list_or_404, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import datetime

# Create your views here.
def home(request, **kwargs):
    if kwargs.get('category_name'):
        posts = get_list_or_404(Post, status=True, category__name=kwargs.get('category_name'), published_date__lt=datetime.datetime.now())
    elif kwargs.get('author'):
        posts = get_list_or_404(Post, status=True, author__username=kwargs.get('name'), published_date__lt=datetime.datetime.now())
    else:
        posts = get_list_or_404(Post, status=True, published_date__lt=datetime.datetime.now())
        
    # posts = Post.objects.filter(status=True)
    # if category_name:
    #     posts = posts.filter(category__name=category_name)
    
    posts = Paginator(posts, 2)
    try:
        page_number = request.GET.get('page_number')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
 
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context=context)


def single(request, id):
    post = get_object_or_404(Post, pk=id, published_date__lt=datetime.datetime.now(), status=True)
    # post = Post.objects.exclude(published_date__gt=datetime.datetime.now()).exclude(status=False).get(id=id)
    # print(post.counted_views)
    post.counted_views += 1
    post.save()
    context = {'post': post}
    return render(request, "blog/blog-single.html", context=context)


def test(request):
    return render(request, "test/test.html")


def search_form(request):
    posts = Post.objects.filter(status=1)
    if world:=request.GET.get('search'):
        posts = posts.filter(content__contains=world)
    context = {'posts': posts}
    return render(request, "blog/blog-home.html", context=context)


def formTest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        print(name, subject)
    else:
        print('request type is not post')

    return render(request, "blog/form.html")