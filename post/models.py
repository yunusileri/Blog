from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=128, verbose_name='Başlık')
    text = models.TextField(verbose_name='İçerik')
    publishing_date = models.DateTimeField(verbose_name='Yayımlanma Tarihi')

    def __str__(self):
        return self.title
