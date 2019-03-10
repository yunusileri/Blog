from django.shortcuts import render, HttpResponse, get_object_or_404, HttpResponseRedirect, redirect, Http404
from .models import Post
from .form import PostForm
from django.contrib import messages
from django.utils.text import slugify

# Create your views here.


def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})


def post_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    contex = {
        'posts': posts,
    }
    return render(request, 'post/detail.html', contex)


def post_create(request):
    if not request.user.is_authenticated:
        return Http404()
    forms = PostForm(request.POST or None, request.FILES or None)
    if forms.is_valid():
        post = forms.save()

        messages.success(request, 'Başarılı Bir Şekilde Oluşturdunuz.', extra_tags='mesaj-basarili')
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'forms': forms}
    return render(request, 'post/form.html', context)

    # if request.method == "POST":
    #     # Formdan Gelen Bilgileri Kaydet
    #     forms = PostForm(request.POST)
    #     if forms.is_valid():
    #         forms.save()
    # else:
    #     # Formu Kullanıcıya Göster
    #     forms = PostForm()

    # Üstteki Satırlar da Aynı işi yapar
    #  forms = PostForm(request.POST or None) Post dolu geldiyse parametre olarak al demektir.


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
    # return HttpResponse('Burası Post update')


def post_delete(request, slug):
    if not request.user.is_authenticated:
        return Http404()
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return redirect('post:index')
