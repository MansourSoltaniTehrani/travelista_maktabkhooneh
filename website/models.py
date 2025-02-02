from django.db import models

# Create your models here.
class Contact(models.Model):
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    updated_date = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    subject = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    published_date = models.DateTimeField(null=True)
    

    class Meta:
        ordering = ('created_date',)

    def __str__(self):
        return self.name


# class Cont(models.Model):
#     created_date = models.DateTimeField(auto_now_add=True)
#     updated_date = models.DateTimeField(auto_now=True)
#     name = models.CharField(max_length=255)
#     subject = models.CharField(max_length=255, null=True)
#     email = models.EmailField(null=True)
#     message = models.TextField(null=True)

#     class Meta:
#         ordering = ('updated_date',)

#     def __str__(self):
#         return self.name
