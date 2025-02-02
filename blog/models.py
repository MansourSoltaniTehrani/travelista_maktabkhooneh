from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name
    
    
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=255)
    category = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    content = models.TextField()
    counted_views = models.IntegerField(default=0) 
    status =  models.BooleanField(default=False)
    published_date =  models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_date',)
        verbose_name = 'post'
        verbose_name_plural = 'postsss'

    def __str__(self):
        return fr"{self.id}_{self.title}"
    
    def trunc(self):
        return self.content[-50:] + "..."
    
    def get_absolute_url(self):
        return reverse('blog:blog_single', kwargs={'id':self.id})
    


    
