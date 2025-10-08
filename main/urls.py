from django.urls import path
from main.views import show_main
from . import views
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_item
from main.views import delete_item
from main.views import add_item_entry_ajax


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),    # list item
    path('add/', views.create_item, name='create_item'),  # form tambah item
    path('<uuid:id>/', views.show_item, name='show_item'), # detail item (UUID)
    path("xml/", views.show_xml, name="show_xml"),        # ← endpoint XML
    path('json/', views.show_json, name='show_json'),   # ← endpoint JSON
    path("xml/<uuid:id>/", views.show_xml_by_id, name="show_xml_by_id"),
    path("json/<uuid:id>/", views.show_json_by_id, name="show_json_by_id"),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('item/<uuid:id>/edit', edit_item, name='edit_item'),
    path('item/<uuid:id>/delete', delete_item, name='delete_item'),
    path("items/add-ajax/", add_item_entry_ajax, name="add_item_entry_ajax"),

]