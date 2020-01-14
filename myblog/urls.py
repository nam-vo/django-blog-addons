from django.urls import path
from myblog.views import PostListView, PostCreateView, PostDetailView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog_index'),
    path('add/', PostCreateView.as_view(), name='blog_add'),
    path('<int:pk>/', PostDetailView.as_view(), name='blog_detail'),
    path('delete/<int:pk>/', PostDeleteView.as_view(), name='blog_delete'),
]