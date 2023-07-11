from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post'),
    path('category/<int:pk>/', views.PostListByCategory.as_view(), name="post-by-category"),
    path('search/', views.PostListSearch.as_view(), name="post-search"),
]