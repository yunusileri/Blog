from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import Post


# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, id):
    posts = get_object_or_404(Post, id=id)
    contex = {
        'posts': posts,
    }
    return render(request, 'post/detail.html', contex)


def post_create(request):
    return HttpResponse('Burası Post create')


def post_update(request):
    return HttpResponse('Burası Post update')


def post_delete(request):
    return HttpResponse('Burası Post delete')
