# main/tests.py
from django.test import TestCase, Client

class PFShopTestCase(TestCase):
    def setUp(self):
        # Buat product dummy untuk context
        self.product = {
            "name": "Adidas Predator Acceler 1998 Red White Black",
            "price": 32907538,  # sekarang berupa int
            "stock": 1,
            "brand": "Adidas",
            "size": "Us8,5 Fr42",
            "category": "Shoes",
            "is_featured": True,
            "description": (
                "Step back into football history with iconic style and unstoppable control. The legendary Predator Acceler 1998 returns in bold red, white, and black, combining classic design with modern comfort. Own the pitch, own the moment."
            ),
            "thumbnail": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.soccerbible.com%2Fperformance%2Ffootball-boots%2F2018%2F08%2Fadidas-reissue-the-1998-predator-accelerator-blackwhitered%2F&psig=AOvVaw1RKg9NCwI7tgzAjmj9Dtve&ust=1757300224276000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCJC528_TxY8DFQAAAAAdAAAAABAE"
        }

    def test_main_url_exists(self):
        """Pastikan halaman utama bisa diakses"""
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_uses_correct_template(self):
        """Pastikan template yang digunakan main.html"""
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')

    def test_product_context_values(self):
        """Pastikan context 'product' berisi data yang benar"""
        response = Client().get('/')
        product = response.context['product']

        self.assertEqual(product['name'], self.product['name'])
        self.assertEqual(product['price'], self.product['price'])
        self.assertEqual(product['stock'], self.product['stock'])
        self.assertEqual(product['brand'], self.product['brand'])
        self.assertEqual(product['size'], self.product['size'])
        self.assertEqual(product['category'], self.product['category'])
        self.assertEqual(product['is_featured'], self.product['is_featured'])
        self.assertEqual(product['description'], self.product['description'])
        self.assertEqual(product['thumbnail'], self.product['thumbnail'])
