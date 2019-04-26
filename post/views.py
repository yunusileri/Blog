from django.http import JsonResponse
from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .form import PostForm, CommentForm
from django.contrib import messages
from django.utils.text import slugify
import json
from django.core import serializers


def post_index(request):
    post = Post.objects.all()
    return render(request, 'post/index.html', {'posts': post})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    form = CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        return HttpResponseRedirect(post.get_absolute_url())

    contex = {
        'post': post,
        'form': form,
    }
    return render(request, 'post/detail.html', contex)


def post_create(request):
    if not request.user.is_authenticated:
        return Http404()
    forms = PostForm(request.POST or None, request.FILES or None)
    if forms.is_valid():
        post = forms.save(commit=False)
        post.user = request.user
        post.save()

        messages.success(request, 'Başarılı Bir Şekilde Oluşturdunuz.', extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'forms': forms}
    return render(request, 'post/form.html', context)


def post_update(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    forms = PostForm(request.POST or None, request.FILES or None, instance=post)
    if forms.is_valid():
        forms.save()
        messages.success(request, 'Başarılı Bir Şekilde Güncellediniz.')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'forms': forms}
    return render(request, 'post/form.html', context)


def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')


def all_post(request):
    data = serializers.serialize('json', Post.objects.all())
    file = open('JSON.txt', 'w')
    file.write(data)
    file.close()
    return JsonResponse(data, safe=False)


def create_post_api(requests):
    post = Post()
    post.user = requests.user
    post.title = requests.GET.get('title')
    post.text = requests.GET.get('text')
    post.save()
    return JsonResponse(json.dumps({'statu': 'Tamam Reis'}), safe=False)


def delete_post_api(requests):
    print(requests.GET.get('slug'))
    post = get_object_or_404(Post, slug=requests.GET.get('slug'))
    post.delete()
    return JsonResponse(json.dumps({'status': 'Tamam Reis'}), safe=False)


def update_post_api(requests):
    post = get_object_or_404(Post, slug=requests.GET.get('slug'))
    post.text = requests.GET.get('text')
    post.title = requests.GET.get('title')
    post.save()
    return JsonResponse(json.dumps({'status': 'Tamam Reis'}), safe=False)
