from django.shortcuts import render, HttpResponse, \
    get_object_or_404, HttpResponseRedirect,redirect
from .models import Post
from .form import PostForm


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
    forms = PostForm(request.POST or None)
    if forms.is_valid():
        post = forms.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'forms': forms}
    return render(request, 'post/form.html', context)


def post_update(request, id):
    post = get_object_or_404(Post, id=id)
    forms = PostForm(request.POST or None, instance=post)
    if forms.is_valid():
        forms.save()
        return HttpResponseRedirect(post.get_absolute_url())
    context = {'forms': forms}
    return render(request, 'post/form.html', context)
    # return HttpResponse('Burası Post update')


def post_delete(request, id):
    post = get_object_or_404(Post, id=id)
    post.delete()
    return redirect('post:index')
