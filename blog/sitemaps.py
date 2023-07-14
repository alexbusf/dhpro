from .models import Post
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

"""Какрта сайта для блога"""
class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.date
    

"""Карта-сайта для статичных страниц"""
class StaticSitemap(Sitemap):

    def items(self):
        return ['osago']
    
    def location(self, item):
        return reverse(item)
