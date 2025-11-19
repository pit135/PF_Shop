# authentication/views.py
import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
from django.http import JsonResponse
import json
from django.contrib.auth import logout as auth_logout
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from main.models import Item


@csrf_exempt
def login(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method.",
        }, status=405)

    username = request.POST.get('username', '')
    password = request.POST.get('password', '')

    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        return JsonResponse({
            "status": True,
            "username": user.username,
            "message": "Login successful!",
        }, status=200)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, please check your username or password.",
        }, status=401)


@csrf_exempt
def register(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": "error",
            "message": "Invalid request method.",
        }, status=405)

    data = json.loads(request.body)

    username = data.get('username', '')
    password1 = data.get('password1', '')
    password2 = data.get('password2', '')

    if password1 != password2:
        return JsonResponse({
            "status": "error",
            "message": "Password dan konfirmasi tidak sama.",
        }, status=400)

    if User.objects.filter(username=username).exists():
        return JsonResponse({
            "status": "error",
            "message": "Username sudah dipakai.",
        }, status=400)

    user = User.objects.create_user(username=username, password=password1)
    user.save()

    return JsonResponse({
        "status": "success",
        "message": "Berhasil register!",
    }, status=201)


@csrf_exempt
def logout(request):
    if request.method != 'POST':
        return JsonResponse({
            "status": False,
            "message": "Invalid request method.",
        }, status=405)

    auth_logout(request)
    return JsonResponse({
        "status": True,
        "message": "Successfully logged out.",
    }, status=200)

@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)
    

@csrf_exempt
def create_item_flutter(request):
    # Pastikan request adalah POST
    if request.method == 'POST':
        try:
            # 1. Baca dan parse JSON dari body request
            data = json.loads(request.body)
            
            # 2. Ambil data dari JSON (Pastikan nama field sama persis!)
            name = data.get("name")
            description = data.get("description")
            thumbnail = data.get("thumbnail")
            # Pastikan tipe data int/bool dikonversi dengan aman
            price = int(data.get("price", 0))
            stock = int(data.get("stock", 0))
            brand = data.get("brand")
            size = data.get("size")
            category = data.get("category")
            is_featured = bool(data.get("is_featured", False))
            
            # 3. Buat dan simpan objek Item baru
            new_product = Item.objects.create(
                user=request.user, # Asumsi Anda menggunakan login_required
                name=name,
                description=description,
                thumbnail=thumbnail,
                price=price,
                stock=stock,
                brand=brand,
                size=size,
                category=category,
                is_featured=is_featured,
            )
            
            # 4. Beri respon sukses
            return JsonResponse({'status': 'success', 'message': 'Produk berhasil disimpan!'})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
        except Exception as e:
            # Beri respon error jika ada masalah lain (misalnya validasi model gagal)
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)

    # Beri respon error jika bukan metode POST
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


@csrf_exempt
def logout(request):
    username = request.user.username
    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logged out successfully!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout failed."
        }, status=401)