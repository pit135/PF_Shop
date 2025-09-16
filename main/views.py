from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ItemForm
from .models import Item

def show_main(request):
    items = Item.objects.all().order_by("-created_at")  # tampilkan terbaru dulu
    context = {
        'name': 'Petrus Wermasaubun',
        'class': "PBP B",
        'item_list': items,  # ganti dari news_list -> item_list
  
    }

    return render(request, "main.html", context)

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, "Item berhasil ditambahkan.")
            return redirect("main:show_item", id=obj.pk)  # PRG: redirect ke detail
    else:
        form = ItemForm()
    return render(request, "add_item.html", {"form": form})

def show_item(request, id):
    item = get_object_or_404(Item, pk=id)  # id = UUID
    return render(request, "item_detail.html", {"item": item})