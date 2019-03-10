from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.
class Post(models.Model):
    user = models.ForeignKey('auth.User', verbose_name='Yazar', on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=128, verbose_name='Başlık')
    text = RichTextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='Yayımlanma Tarihi', auto_now_add=True)
    # image = models.FileField(null=True, blank=True)   # Filefield mp3 vs eklerken de kullanılabilir
    image = models.ImageField(null=True, blank=True)
    slug = models.SlugField(unique=True, editable=False, max_length=130)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post:detail', kwargs={'id': self.id})
        return reverse('post:detail', kwargs={'slug': self.slug})
        # return "/post/{}".format(self.id)

    def get_create_url(self):
        return reverse('post:create')

    def get_update_url(self):
        # return reverse('post:update', kwargs={'id': self.id})
        return reverse('post:update', kwargs={'slug': self.slug})

    def get_delete_url(self):
        # return reverse('post:delete', kwargs={'id': self.id})
        return reverse('post:delete', kwargs={'slug': self.slug})

    def get_unique_slug(self):
        slug = slugify(self.title.replace('ı', 'i'))
        uniqe_slug = slug
        counter = 1
        while Post.objects.filter(slug=uniqe_slug).exists():
            uniqe_slug = f'{slug}-{counter}'
            counter += 1
        return uniqe_slug

    def save(self, *args, **kwargs):
        # if not self.slug: # Bunu açarsak Slug Alanı Asla Güncellenmez 1 kere Oluşturulur
        self.slug = self.get_unique_slug()
        return super(Post, self).save(*args, **kwargs)

    # Postların Görünümünü Sıralamak için
    class Meta:
        ordering = ['-publishing_date']


class Comment(models.Model):
    post = models.ForeignKey('post.Post', related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, verbose_name='İsim')
    content = models.TextField(verbose_name='İçerik')
    createdDate = models.DateTimeField(auto_now_add=True)
