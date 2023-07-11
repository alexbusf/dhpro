from .models import Post
from django.contrib.sitemaps import Sitemap

"""Какрта сайта для блога"""
class BlogSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.8

    def items(self):
        return Post.objects.all()
    
    def lastmod(self, obj):
        return obj.date
