# main/tests.py
from django.test import TestCase, Client
from django.test import TestCase, Client
from .models import Item
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from django.contrib.auth.models import User

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

