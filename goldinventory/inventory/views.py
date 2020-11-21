from django.shortcuts import render
from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_earrings(request):
    items = earring.objects.all()

    context = {
        'items': items,

    }
    # this render this html file with  these items in context
    return render(request, 'index.html', context)


def display_rings(request):
    items = rings.objects.all()

    context = {
        'items': items,

    }
    # this render this html file with  these items in context
    return render(request, 'index.html', context)


def display_diamonds(request):
    items = diamonds.objects.all()

    context = {
        'items': items,

    }
    # this render this html file with  these items in context
    return render(request, 'index.html', context)
