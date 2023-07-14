from .models import Post, Category
from django.views import generic
from django.db.models import Q
from django.http import Http404

"""All posts"""
class PostList(generic.ListView):
    model = Post
    paginate_by = 5

"""Post by category"""
class PostListByCategory(generic.ListView):
    model = Post
    paginate_by = 5
    category = None
    template_name="blog/post_list_by_category.html"

    def get_queryset(self):
        try:
            self.category = Category.objects.get(slug=self.kwargs['slug'])
            queryset = Post.objects.all().filter(category_id=self.category.id)
            return queryset
        except:
            raise Http404("Category does not exist")
    

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
