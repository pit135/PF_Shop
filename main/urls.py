from django.urls import path
from main.views import show_main
from . import views

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),    # list item
    path('add/', views.create_item, name='create_item'),  # form tambah item
    path('<uuid:id>/', views.show_item, name='show_item') # detail item (UUID)
]