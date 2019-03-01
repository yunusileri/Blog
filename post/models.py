from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Başlık')
    text = models.TextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='Yayımlanma Tarihi', auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post:detail', kwargs={'id': self.id})
        # return "/post/{}".format(self.id)
