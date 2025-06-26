from django.shortcuts import render
from django.views import generic
from .models import Post
from django.http import HttpResponse


# Create your views here.
class PostList(generic.ListView):
<<<<<<< HEAD
    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginate_by = 6
=======

    queryset = Post.objects.filter(status=1)
    template_name = "blog/index.html"
    paginated_by = 6
>>>>>>> dab80e7959907c74c1c99ef770129302f400505b
