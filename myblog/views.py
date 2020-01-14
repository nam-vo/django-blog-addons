from django.shortcuts import render
from django.http import Http404

from myblog.models import Post
from myblog.forms import PostForm, CategoryForm

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from myblog.serializers import UserSerializer, GroupSerializer

class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # fields = '__all__'

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('blog_index')

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer