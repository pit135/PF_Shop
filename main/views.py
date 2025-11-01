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
from datetime import datetime
from django.utils.html import strip_tags

@login_required(login_url='/login/')
def show_main(request):
    # coba ambil dari cookie dulu
    cookie_last_login = request.COOKIES.get("last_login")

    # kalau cookie gak ada, pakai field bawaan user
    if cookie_last_login:
        last_login = cookie_last_login
    else:
        # request.user.last_login bisa None
        if request.user.last_login:
            last_login = request.user.last_login.strftime("%Y-%m-%d %H:%M:%S")
        else:
            last_login = "Never"

    context = {
        "last_login": last_login,
    }
    return render(request, "main.html", context)

@login_required(login_url='/login/')
def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user         
            item.save()                   
            return redirect("main:show_main")
    else:
        form = ItemForm()

    return render(request, "add_item.html", {"form": form})

@login_required(login_url='/login')
def show_item(request, id):
    item = get_object_or_404(Item, pk=id)  # id = UUID
    return render(request, "item_detail.html", {"item": item})

def show_xml(request):
    items = Item.objects.all()                       # ambil semua Item
    xml_data = serializers.serialize("xml", items)   # serialize ke XML
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items = Item.objects.all().order_by('-created_at')
    data = []
    for item in items:
        data.append({
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
            "created_at": item.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
            "user_id": str(item.user.id) if item.user else None,
        })
    return JsonResponse(data, safe=False)


def show_xml_by_id(request, id):
    item_qs = Item.objects.filter(pk=id)                
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
            response = JsonResponse({'message': 'Account created successfully!'}, status=200)
            response.set_cookie('toast', 'Registration successful!')
            return response
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    form = UserCreationForm()
    return render(request, "register.html", {'form': form})

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = JsonResponse({'message': 'Login successful!'}, status=200)
            now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            response.set_cookie('last_login', now_str)
            response.set_cookie('toast', 'Login successful!')  # toast cookie
            return response
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = AuthenticationForm(request)
    return render(request, "login.html", {'form': form})


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.set_cookie('toast', 'Logged out successfully!')  # toast cookie
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def edit_item(request, id):
    item = get_object_or_404(Item, pk=id, user=request.user)
    form = ItemForm(request.POST or None, instance=item)

    if request.method == "POST":
        if form.is_valid():
            form.save()
            # kalau dari modal / fetch
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"message": "Item updated"}, status=200)
            # kalau submit biasa
            return redirect("main:show_main")
        else:
            if request.headers.get("x-requested-with") == "XMLHttpRequest":
                return JsonResponse({"errors": form.errors}, status=400)

    return render(request, "edit_item.html", {"form": form})

@login_required(login_url='/login/')
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id, user=request.user)
    item.delete()
    return redirect("main:show_main")
    
@csrf_exempt
@require_POST
@login_required(login_url='/login/')
def add_item_entry_ajax(request):
    form = ItemForm(request.POST)
    if form.is_valid():
        item = form.save(commit=False)
        item.user = request.user
        item.save()
        return JsonResponse({
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
            "created_at": item.created_at.strftime("%Y-%m-%dT%H:%M:%S"),
            "user_id": str(item.user.id),
        })
    return JsonResponse({"errors": form.errors}, status=400)

