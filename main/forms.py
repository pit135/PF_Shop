# main/forms.py
from django.forms import ModelForm
from .models import Item
from django.utils.html import strip_tags

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "stock", "brand", "size",
                  "category", "is_featured", "description", "thumbnail"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_stock(self):
        stock = self.cleaned_data["stock"]
        return strip_tags(stock)
    
    def clean_brand(self):
        brand = self.cleaned_data["brand"]
        return strip_tags(brand)
    
    def clean_size(self):
        size = self.cleaned_data["size"]
        return strip_tags(size)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)