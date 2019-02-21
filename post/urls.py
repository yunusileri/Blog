from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('index/', post_index),
    # path('{}'.format(id), post_detail),
    path('<id>/', post_detail),
    path('create/', post_create),
    path('update/', post_update),
    path('delete/', post_delete),
]
