from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.PostList.as_view(), name='posts'),
    path('<int:pk>/', views.PostDetail.as_view(), name='post'),
    path('category/<str:slug>/', views.PostListByCategory.as_view(), name="post-by-category"),
    path('search/', views.PostListSearch.as_view(), name="post-search"),
    path('osago/', TemplateView.as_view(template_name="blog/osago.html"), name="osago"),
    path('debetcard/', TemplateView.as_view(template_name="blog/debetcard.html"), name="debetcard"),
    path('creditcard/', TemplateView.as_view(template_name="blog/creditcard.html"), name="creditcard"),
    path('microcredit/', TemplateView.as_view(template_name="blog/microcredit.html"), name="microcredit"),
    path('credit/', TemplateView.as_view(template_name="blog/credit.html"), name="credit"),
    path('rco/', TemplateView.as_view(template_name="blog/rco.html"), name="rco"),
    path('deposit/', TemplateView.as_view(template_name="blog/deposit.html"), name="deposit"),
    path('hypothec/', TemplateView.as_view(template_name="blog/hypothec.html"), name="hypothec"),
]