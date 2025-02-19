from django.contrib.sitemaps import Sitemap
from blog.models import Post
from django.urls import reverse


class BlogSitemap(Sitemap):
    changefreq = "never"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
    
    def location(self, items):
        return reverse('blog:blog_single', kwargs={'id':items.id})