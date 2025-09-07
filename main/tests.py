# main/tests.py
from django.test import TestCase, Client

class PFShopTestCase(TestCase):
    def setUp(self):
        # Buat product dummy untuk context
        self.product = {
            "name": "Petrus Wermasaubun",
            "class": "PBP B",
        }

    def test_main_url_exists(self):
        """Pastikan halaman utama bisa diakses"""
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)

    def test_main_uses_correct_template(self):
        """Pastikan template yang digunakan main.html"""
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')