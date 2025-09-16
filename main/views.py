from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ItemForm
from .models import Item
from django.http import HttpResponse
from django.core import serializers

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

def show_xml(request):
    items = Item.objects.all()                       # ambil semua Item
    xml_data = serializers.serialize("xml", items)   # serialize ke XML
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items = Item.objects.all()                      # ambil semua Item
    json_data = serializers.serialize("json", items)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    item_qs = Item.objects.filter(pk=id)                 # queryset (bisa kosong jika tidak ada)
    xml_data = serializers.serialize("xml", item_qs)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    item = Item.objects.get(pk=id)                       # akan error 404 jika id tidak ada
    json_data = serializers.serialize("json", [item])    # bungkus list untuk serialize satu objek
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return HttpResponse(status=404)
    xml_data = serializers.serialize("xml", [item])
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    try:
        item = Item.objects.get(pk=id)
    except Item.DoesNotExist:
        return HttpResponse(status=404)
    json_data = serializers.serialize("json", [item])
    return HttpResponse(json_data, content_type="application/json")