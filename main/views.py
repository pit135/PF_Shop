from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ItemForm
from .models import Item
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        item = Item.objects.all()
    else:
        item = Item.objects.filter(user=request.user)

    context = {
        'name': 'Petrus Wermasaubun',
        'class': "PBP B",
        'item_list': item,  # ganti dari news_list -> item_list
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }
    return render(request, "main.html", context)

def create_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()  # Simpan item baru
            return JsonResponse({'message': 'Item created successfully!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    form = ItemForm()
    return render(request, "add_item.html", {'form': form})

@login_required(login_url='/login')
def show_item(request, id):
    item = get_object_or_404(Item, pk=id)  # id = UUID
    return render(request, "item_detail.html", {"item": item})

def show_xml(request):
    items = Item.objects.all()                       # ambil semua Item
    xml_data = serializers.serialize("xml", items)   # serialize ke XML
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    item_list = Item.objects.all()
    data = [
        {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'stock': item.stock,
            'brand': item.brand,
            'size': item.size,
            'category': item.category,
            'is_featured': item.is_featured,
            'description': item.description,
            'thumbnail': item.thumbnail,
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'user_id': item.user_id,
        }
        for item in item_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, id):
    item_qs = Item.objects.filter(pk=id)                 # queryset (bisa kosong jika tidak ada)
    xml_data = serializers.serialize("xml", item_qs)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    try:
        item = Item.objects.select_related('user').get(pk=id)
        data = {
            'id': str(item.id),
            'name': item.name,
            'price': item.price,
            'stock': item.stock,
            'brand': item.brand,
            'size': item.size,
            'category': item.category,
            'is_featured': item.is_featured,
            'description': item.description,
            'thumbnail': item.thumbnail,
            'created_at': item.created_at.isoformat() if item.created_at else None,
            'user_id': item.user_id,
            'user_username': item.user.username if item.user_id else None,
        }
        return JsonResponse(data)
    except Item.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Account created successfully!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return render(request, "register.html", {'form': form})

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)  # Login user
        return JsonResponse({'message': 'Login successful!'}, status=200)  # Return success message
      else:
        # If form is not valid, return error messages
        return JsonResponse({'errors': form.errors}, status=400)

   else:
      form = AuthenticationForm(request)  # On GET request, create an empty form
   return render(request, "login.html", {'form': form})  # Render login page on GET request


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'message': 'Item updated successfully!'}, status=200)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    
    form = ItemForm(instance=item)
    return render(request, "edit_item.html", {'form': form})

def delete_item(request, id):
    try:
        # Cek jika item ada
        item = get_object_or_404(Item, pk=id)
        item.delete()  # Hapus item

        # Mengembalikan respons JSON jika penghapusan berhasil
        return JsonResponse({'message': 'Item deleted successfully!'}, status=200)

    except Item.DoesNotExist:
        # Mengembalikan respons error jika item tidak ditemukan
        return JsonResponse({'message': 'Item not found'}, status=404)
    
@csrf_exempt
@require_POST
def add_item_entry_ajax(request):
    # # ambil & normalisasi data POST
    name        = strip_tags(request.POST.get("name") or "").strip()
    price_raw   = strip_tags(request.POST.get("price"))
    stock_raw   = strip_tags(request.POST.get("stock"))
    brand       = strip_tags(request.POST.get("brand") or "").strip()
    size        = strip_tags(request.POST.get("size") or "").strip()                  # optional
    category    = request.POST.get("category")
    is_featured = (request.POST.get("is_featured") in ["on", "true", "True", "1"])
    description = strip_tags(request.POST.get("description") or "").strip()
    thumbnail   = (request.POST.get("thumbnail") or "").strip() or None     # optional
    user        = request.user

    # validasi sederhana
    errors = {}
    if not name:
        errors["name"] = "This field is required."
    if price_raw in (None, ""):
        errors["price"] = "This field is required."
    else:
        try:
            price = int(price_raw)
        except (TypeError, ValueError):
            errors["price"] = "Must be an integer."

    if stock_raw in (None, ""):
        errors["stock"] = "This field is required."
    else:
        try:
            stock = int(stock_raw)
        except (TypeError, ValueError):
            errors["stock"] = "Must be an integer."

    if not brand:
        errors["brand"] = "This field is required."

    # validasi pilihan kategori
    valid_categories = dict(Item.CATEGORY_CHOICES).keys()
    if not category or category not in valid_categories:
        errors["category"] = f"Invalid category. Must be one of: {', '.join(valid_categories)}"

    if not description:
        errors["description"] = "This field is required."

    if errors:
        return JsonResponse({"ok": False, "errors": errors}, status=400)

    # create item
    item = Item.objects.create(
        user=user,
        name=name,
        price=price,
        stock=stock,
        brand=brand,
        size=size,
        category=category,
        is_featured=is_featured,
        description=description,
        thumbnail=thumbnail,
    )

    # response JSON (cocok dengan show_json_by_id kamu)
    return JsonResponse({
        "ok": True,
        "id": str(item.id),
        "name": item.name,
        "price": item.price,
        "stock": item.stock,
        "brand": item.brand,
        "size": item.size,
        "category": item.category,
        "is_featured": item.is_featured,
        "description": item.description,
        "thumbnail": item.thumbnail,
        "created_at": item.created_at.isoformat() if item.created_at else None,
        "user_id": item.user_id,
        "user_username": item.user.username if item.user_id else None,
    }, status=201)


