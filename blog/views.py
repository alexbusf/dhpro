from .models import Post, Category
from django.views import generic
from django.db.models import Q

"""All posts"""
class PostList(generic.ListView):
    model = Post

"""Post by category"""
class PostListByCategory(generic.ListView):
    model = Post
    category = None

    def get_queryset(self):
        self.category = Category.objects.get(pk=self.kwargs['pk'])
        queryset = Post.objects.all().filter(category_id=self.category.id)
        return queryset
    

"""Post search"""
class PostListSearch(generic.ListView):
    model = Post

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Post.objects.all().filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return queryset
    

"""Post detail"""
class PostDetail(generic.DetailView):
    model = Post
