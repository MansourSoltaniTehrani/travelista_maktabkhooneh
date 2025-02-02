from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()

@register.simple_tag(name="test")
def func(name):
    return f"Hello, {name}!"

@register.simple_tag(name="query")
def func():
    posts = Post.objects.filter(status=True)
    return posts


@register.filter(name='snippet')
def func(text, count=100):
    return text[:count]


@register.inclusion_tag(name="latest_pots", filename="latest_posts.html")
def func(count=2):
    posts = Post.objects.filter(status=True).exclude(published_date__gt=timezone.now()).order_by('-updated_date')[:count]
    return {'posts':posts}


# @register.inclusion_tag(name="category_list", filename="blog/category_list.html")
# def  func():
#     categories = Category.objects.all()
    
#     count_dict = {}
#     for category in categories:
#         post_counts = Post.objects.filter(category__name=category).count()
#         count_dict[category] = post_counts
#     return {'count_dict': count_dict}

@register.inclusion_tag(name="category_list", filename="blog/category_list.html")
def func():
    counted_dict = {}
    category = Category.objects.all()
    for each_cat in category:
        counted_dict[each_cat] = Post.objects.filter(category__name=each_cat).count() 
    return {'count_dict':counted_dict}

@register.inclusion_tag(name='blog_single_nav_area', filename='blog/blog_single_nav_area.html')
def func(post_id):
    posts = Post.objects.all().exclude(status=False).exclude(published_date__gt=timezone.now()).order_by('created_date')
    # print(post_id)
    # print(posts)
    first_post_id = posts[0].id
    post_id -= first_post_id-1
    # last_post_id = posts[-1].id
    # print(first_post_id, post_id, end='//////////')
    if post_id<len(posts) and post_id>1 :
        prev_post = posts[post_id-2]
        next_post = posts[post_id]
    elif post_id<len(posts) and post_id==1:
        prev_post = None
        next_post = posts[post_id]
    elif post_id==len(posts) and post_id>1:
        prev_post = posts[post_id-2]
        next_post = None
    else:
        prev_post, next_post = None, None

    # print(prev_post,next_post, end="****************")

    return {'next_post':next_post, 'prev_post':prev_post}
    