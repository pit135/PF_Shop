from django.db import models
import uuid

class Item(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('shoes', 'Shoes'),
        ('ball', 'Ball'),
        ('accessory', 'Accessory'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)                # nama item
    price = models.IntegerField()                          # Harga item
    stock = models.PositiveIntegerField(default=0)         # Stok item
    brand = models.CharField(max_length=100)               # Brand (misal: Adidas, Nike)
    size = models.CharField(max_length=50, blank=True)     # Ukuran (misal: US8.5, FR42)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)       # Status unggulan
    description = models.TextField()                       # Deskripsi
    thumbnail = models.URLField(blank=True, null=True)     # Link gambar
    created_at = models.DateTimeField(auto_now_add=True)   # Otomatis isi waktu dibuat
