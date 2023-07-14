from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post'),
    path('category/<str:slug>/', views.PostListByCategory.as_view(), name="post-by-category"),
    path('search/', views.PostListSearch.as_view(), name="post-search"),
    path('osago/', TemplateView.as_view(template_name="blog/osago.html"), name="osago"),
]