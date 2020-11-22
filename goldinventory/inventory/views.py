from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_earrings(request):
    items = earring.objects.all()

    context = {
        'items': items,
        'header': 'earrings'

    }
    # this render this html file with  these items in context
    return render(request, 'index.html', context)


def display_rings(request):
    items = rings.objects.all()

    context = {
        'items': items,
        'header': 'rings'

    }
    # this render this html file with  these items in context
    return render(request, 'index.html', context)


def display_diamonds(request):
    items = diamonds.objects.all()

    context = {
        'items': items,
        'header': 'diamonds'

    }
    # this render this html file with  these items in context
    return render(request, 'index.html', context)


def add_device(request, cls):
    if request.method == 'POST':
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls()
        return render(request, 'add_new.html', {'form': form})


def add_earrings(request):
    return add_device(request, earringForm)


def add_rings(request):
    return add_device(request, ringForm)


def add_diamonds(request):
    return add_device(request, diamondForm)


def edit_device(request, id, model, cls):
    item = get_object_or_404(model, id=id)

    if request.method == "POST":

        form = cls(request.POST, instance=item)

        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})


def edit_earrings(request, id):
    return edit_device(request, id, earring, earringForm)


def edit_rings(request, id):
    return edit_device(request, id, rings, ringForm)


def edit_diamonds(request, id):
    return edit_device(request, id, diamonds, diamondForm)


def delete_earrings(request, id):
    earring.objects.filter(id=id).delete()

    items = earring.objects.all()
    context = {
        'items': items
    }

    return render(request, 'index.html', context)


def delete_rings(request, id):
    rings.objects.filter(id=id).delete()

    items = rings.objects.all()
    context = {
        'items': items
    }

    return render(request, 'index.html', context)


def delete_diamonds(request, id):
    diamonds.objects.filter(id=id).delete()

    items = diamonds.objects.all()
    context = {
        'items': items
    }

    return render(request, 'index.html', context)
