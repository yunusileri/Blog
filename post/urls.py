from django.urls import path, re_path
from .views import *

app_name ='post'


urlpatterns = [
    path('index/', post_index, name='index'),
    path('detail/<id>/', post_detail, name='detail'),  # Bu Tanımlama değişken alır view a aktarır.
    path('create/', post_create, name='create'),
    path('update/<id>/', post_update, name='update'),
    path('delete/<id>/', post_delete, name='delete'),
]
