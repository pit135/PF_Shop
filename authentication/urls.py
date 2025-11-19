from django.urls import include, path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('logout/', views.logout, name='logout'),
    path('create-item-flutter/', views.create_item_flutter, name='create_item_flutter'),
]
