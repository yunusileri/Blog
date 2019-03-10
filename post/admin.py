from django.contrib import admin
from .models import Post


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'publishing_date', 'slug']  # Listelerken Göstermek için
    list_display_links = ['publishing_date', 'title']  # link oluşturmak için
    list_filter = ['publishing_date', 'text']  # Filtreleme yapmak için
    # prepopulated_fields = {'slug': ('title',)} # Görünümden Kaldırdıgımız için kapatmalıyız

    # list_editable = ['title'] #ogeyi listelerken duzenlemek icin kullanılabilir
    # ancak hem link hem duzunleme aynı anda aktif olamaz .

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
