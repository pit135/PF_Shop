# main/forms.py
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "stock", "brand", "size",
                  "category", "is_featured", "description", "thumbnail"]

        widgets = {
        # price jadi text (tanpa spinner), tetap angka biasa saat diketik
        "price": forms.TextInput(attrs={
            "inputmode": "numeric",   # keypad angka di mobile
            "pattern": r"\d*",        # hint: hanya digit
            "placeholder": "12000000"
        }),
        }