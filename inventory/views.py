from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .forms import *

def index(request):
    return render(request,'index.html')

def display_laptops(request):
    items = Laptop.objects.all()
    context = {
        'items': items,
        'header':'laptops',
    }
    return render(request, 'index.html', context)

def display_desktops(request):
    items = Desktop.objects.all()
    context = {
        'items': items,
        'header':'desktops',
    }
    return render(request, 'index.html', context)

def display_mobiles(request):
    items = Mobile.objects.all()
    context = {
        'items': items,
        'header':'mobiles',
    }
    return render(request, 'index.html', context)

def add_device(request,cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('inventory:index')

    else:
        form = cls()
        return render(request, 'add_new.html', {'form' : form})

def add_laptops(request):
    return add_device(request,LaptopForm)

def add_desktops(request):
    return add_device(request,DesktopForm)

def add_mobiles(request):
    return add_device(request,MobileForm)

def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('inventory:index')
    else:
        form = cls(instance=item)

        return render(request, 'edit_item.html', {'form': form})

def edit_laptops(request, pk):
    return edit_item(request, pk, Laptop, LaptopForm)


def edit_desktops(request, pk):
    return edit_item(request, pk, Desktop, DesktopForm)


def edit_mobiles(request, pk):
    return edit_item(request, pk, Mobile, MobileForm)



def delete_laptops(request, pk):

    template = 'index.html'
    Laptop.objects.filter(id=pk).delete()

    items = Laptop.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_desktops(request, pk):

    template = 'index.html'
    Desktop.objects.filter(id=pk).delete()

    items = Desktop.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_mobiles(request, pk):

    template = 'index.html'
    Mobile.objects.filter(id=pk).delete()

    items = Mobile.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)





































