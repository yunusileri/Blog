from django.urls import path, re_path
from .views import *

app_name = 'post'

urlpatterns = [
    path('index/', post_index, name='index'),
    path('detail/<slug>/', post_detail, name='detail'),  # Bu Tanımlama değişken alır view a aktarır.
    path('create/', post_create, name='create'),
    path('update/<slug>/', post_update, name='update'),
    path('delete/<slug>/', post_delete, name='delete'),

    path('all', all_post),
    path('api_create', create_post_api),
    path('api_delete', delete_post_api),
    path('api_update', update_post_api),
]
