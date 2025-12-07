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