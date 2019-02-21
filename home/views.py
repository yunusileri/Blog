from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def home_view(request):
    if request.user.is_authenticated:
        context = {
            'isim': 'yunus',
            'yas': '21',
        }
    else:
        context = {
            'isim': 'Müsafir',
            'yas': '21',
        }
    return render(request, 'home.html', context)
