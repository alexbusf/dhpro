from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse

"""Categories models."""
class Category(models.Model):
    title = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('post-by-category', args=[str(self.id)])
    

"""Posts models."""
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    title = models.CharField('Title', max_length=60)
    description = models.CharField('Description', max_length=160)
    content = RichTextUploadingField(blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-date"]

    def __str__(self):
        return self.title
    
    def get_absolute_url(self): 
        return reverse('post', args=[str(self.id)])
    