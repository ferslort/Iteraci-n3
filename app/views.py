from django.shortcuts import render
from .models import UserCustom

# Create your views here.


def page_index(request):
    return render(request, 'index.html')


def page_user(request):

    users = UserCustom.objects.all()

    return render(request, 'users.html', {
        'users': users
    })
