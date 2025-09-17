Checklist untuk tugas ini adalah sebagai berikut.

1. Membuat sebuah proyek Django baru.
Sebelum membuat proyek Django baru, sesuai yang ada di tutorial diberikan, terdapat beberapa langkah yang harus saya lakukan

a) Membuat akun GitHub.
=> Namun, apa itu Git dan GitHub?
=> Git: Sistem Kontrol Version untuk Codebase
yang membantu melacak perubahan pada kode sumber proyek
=> GitHub: Platform Kolaborasi Menggunakan Git
platform berbasis web yang memungkinkanmu untuk menyimpan, mengelola, dan berkolaborasi pada proyek-proyek menggunakan Git.
=> Mengapa Penting?
Git dan GitHub memainkan peran penting dalam pengembangan perangkat lunak modern dan kolaborasi tim. Keduanya memungkinkan tim untuk melacak perubahan kode, menyimpan versi, dan bekerja bersama dalam proyek secara efisien.
Dalam langkah ini, saya tidak melakukannya lagi, karena sudah pernah membuat akun GitHub saat di semester 2, yaitu pada mata kuliah DDP 2.

b) Instalasi IDE
=> IDE adalah sebuah software yang menyatukan berbagai alat bantu pemrograman dalam satu tempat, supaya programmer bisa menulis, menjalankan, dan mengelola kode dengan lebih mudah. 
Dalam langkah kedua ini juga saya sudah tidak melakukannya lagi, karena saya sudah menginstal IDE (VS Code) dari saya berada di semester 1, untuk mata kuliah DDP 1.

c) Konfigurasi Git
=> Setelah Git terpasang, saya perlu mendaftarkan identitas diri agar setiap commit (penyimpanan perubahan kode) punya nama dan email yang jelas, hal tersebut dinamakan konfigurasi Git.’
Caranya, dengan menjalankan kode di bawah ke terminal.
<!-- git config --global user.name "<NAME>"
git config --global user.email "<EMAIL>" -->
 flag --global akan mengubah konfigurasi global untuk seluruh sistem (saya sedang bilang ke Git: "kalau aku pakai Git di komputer ini, anggap saja namaku dan emailku selalu ini.”)
Langkah ketiga ini saya juga tidak perlu melakukannya,, karena saya sudah pernah melakukan hal tersebut sebelumnya.

d) Konfigurasi Autentikasi
=> Konfigurasi autentikasi adalah cara saya mengatur identitas agar Git percaya saya punya akses ke repository remote. Tanpa konfigurasi autentikasi, Git akan menolak akses (Authentication failed). Ya intinya untuk nantinya menghubungkan akun Git saya dengan akun GitHub
Caranya ialah sbb (u/ mac), karena saya mac user:
<!-- git credential-manager configure
git config --global credential.credentialStore keychain -->

e) Verifikasi Konfigurasi
=> Untuk memastikan konfigurasi telah diatur dengan benar pada repositori lokal, saya bisa jalankan perintah berikut
<!-- git config --list -->

f) Instalasi Django dan Inisiasi Proyek Django
=> Django adalah kerangka kerja (framework) yang populer untuk pengembangan aplikasi web dengan bahasa pemrograman Python. 
Ada beberapa langkah: 

     1) Membuat Direktori dan Mengaktifkan Virtual Environment
- Saya membuat direktori baru dengan nama Football Shop.
- Buka terminal dari direktori tersebut
- Trus, saya buat virtual environment dengan jalankan perintah berikut
<!-- python3 -m venv env -->
(Virtual environment ini berguna untuk mengisolasi package serta dependencies dari aplikasi agar tidak bertabrakan dengan versi lain yang ada pada komputer saya)
- Selanjutnya, saya aktivin virtual environment dengan perintah berikut.
<!-- source env/bin/activate -->
Tanda udah aktif itu dengan (env) di baris input terminal.

     2) Menyiapkan Dependencies dan Membuat Proyek Django
=> Dependencies adalah komponen atau modul yang diperlukan oleh suatu perangkat lunak untuk berfungsi, termasuk library, framework, atau package. Hal tersebut memungkinkan pengembang memanfaatkan kode yang telah ada, mempercepat pengembangan, tetapi juga memerlukan manajemen yang hati-hati untuk memastikan kompatibilitas versi yang tepat. Penggunaan virtual environment membantu mengisolasi dependencies antara proyek-proyek yang berbeda.
- Di dalam direktori yang Football Shop, saya buat berkas requirements.txt trus tambahkan beberapa dependencies (file teks yang berisi daftar semua library Python yang dibutuhkan oleh sebuah proyek.)
<!-- django
gunicorn
whitenoise
psycopg2-binary
requests
urllib3
Python-dotenv -->
-  Selanjutnya, saya instal dependencies yang ada di terminal yang sebelumnya (yg virtual environment nya udh aktif) dengan perintah berikut.
<!-- pip install -r requirements.txt -->
- Setelah itu, saya buat proyek Django namanya  PF_Shop dengan perintah berikut.
<!-- django-admin startproject PF_Shop . -->

     3) Konfigurasi Environment Variables dan Proyek
- Selanjutnya, saya buat file .env di direktori root proyek (dimana file manage.py berada), isi dengan dibawah:
<!-- PRODUCTION=False  -->
artinya aplikasi masih di mode pengembangan, belum di-deploy ke server beneran.


** Environment variables adalah variabel yang disimpan di luar kode program dan digunakan untuk menyimpan informasi konfigurasi seperti kredensial database, API keys, atau pengaturan environment. Ini memungkinkan kode yang sama berjalan di environment berbeda tanpa perlu mengubah kode.


<!-- - Selanjutnya, saya buat file .env.prod di direktori yang sama untuk konfigurasi production trus isi semua yang ada dibawah (tapi datanya sesuaiin sama yang saya dapet di email)
DB_NAME=<nama database>
DB_HOST=<host database>
DB_PORT=<port database>
DB_USER=<username database>
DB_PASSWORD=<password database>
SCHEMA=tugas_individu
PRODUCTION=True -->


** Perbedaan .env dengan .env.prod
=> .env: Digunakan untuk development lokal. Karena PRODUCTION=False, aplikasi akan menggunakan database SQLite yang lebih simple untuk testing dan development
=> .env.prod: Digunakan untuk production deployment. Karena PRODUCTION=True, aplikasi akan menggunakan database PostgreSQL dengan kredensial yang disediakan ITF Fasilkom UI
- Selanjutnya saya modifikasi file settings.py untuk menggunakan environment variables, dan, tambahin kode dibawah ini, dibagian atas setelah import path
<!-- import os
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv() -->
- Setelah itu, saya tambahkan kedua string berikut pada ALLOWED_HOSTS di settings.py untuk keperluan development:
<!-- …
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
... -->
** Dalam konteks deployment, ALLOWED_HOSTS berfungsi sebagai daftar host yang diizinkan untuk mengakses aplikasi web. Dengan menetapkan nilai di atas, saya mengizinkan akses dari host lokal, artinya hanya bisa diakses dari jaringan saya saja. Namun, apabila saya men-deploy aplikasi ke suatu server, pastikan bahwa saya menambahkan host dari server tersebut pada ALLOWED_HOSTS.
- Setelah itu, saya tambahin konfigurasi PRODUCTION di atas code DEBUG di settings.py.
<!-- PRODUCTION = os.getenv('PRODUCTION', 'False').lower() == 'true' -->
** Supaya gak perlu edit file settings.py tiap kali pindah dari laptop (development) ke server (production). Cukup atur environment variable PRODUCTION=True → otomatis Django ngerti dia harus jalan di mode production.
- Setelah itu, saya ubah konfigurasi database di settings.py. Cari bagian DATABASES dan ganti dengan:
<!-- # Database configuration
if PRODUCTION:
    # Production: gunakan PostgreSQL dengan kredensial dari environment variables
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.getenv('DB_NAME'),
            'USER': os.getenv('DB_USER'),
            'PASSWORD': os.getenv('DB_PASSWORD'),
            'HOST': os.getenv('DB_HOST'),
            'PORT': os.getenv('DB_PORT'),
            'OPTIONS': {
                'options': f"-c search_path={os.getenv('SCHEMA', 'public')}"
            }
        }
    }
else:
    # Development: gunakan SQLite
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    } -->
*** Gunanya adalah konfigurasi database dinamis, artinya jenis database yang dipakai akan berbeda tergantung apakah aplikasi jalan di development atau production.
Fleksibel → Bisa beda database antara development dan production.
Aman → Kredensial database tidak disimpan di kode, tapi di environment variable.
Praktis → Developer cukup pakai SQLite, deployment otomatis pakai PostgreSQL.

     4) Jalankan Server
=> Selanjutnya, saya pastikan bahwa berkas manage.py ada di direktori yang aktif di terminal saya saat ini, trus saya jalankan migrasi database dengan perintah:
<!-- python3 manage.py migrate -->
Setelah itu saya jalankan server Django dengan perintah
<!-- python3 manage.py runserver -->
Lalu, untuk cek apakah aplikasi Django saya berhasil atau tidak, saya buka http://localhost:8000 di chrome saya untuk liat animasi roket sebagai tanda berhasil atau tidaknya.

f) Unggah Proyek ke Repositori GitHub
=> Saya buat repositori GitHub baru dengan nama yang sama yaitu PF_Shop, trus inisiasi direktori lokal PF_Shop sebagai repositori Git.
Trus, saya jalankan perintah git init di terminal, gunanya untuk membuat folder .git yang dipake untuk melacak perubahan file secara lokal
=> Setelah itu, saya tambahin berkas .gitignore, merupakan konfigurasi yang digunakan di repositori Git untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git. Berkas ini perlu dibuat karena kadang ada berkas-berkas yang ga perlu dilacak Git, seperti berkas-berkas yang dihasilkan oleh proses kompilasi, berkas sementara, atau berkas konfigurasi pribadi
Isinya seperti dibawah ini:
<!-- # Django
*.log
*.pot
*.pyc
**pycache**
db.sqlite3
media
# Backup files
*.bak
# If you are using PyCharm
# User-specific stuff
.idea/**/workspace.xml
.idea/**/tasks.xml
.idea/**/usage.statistics.xml
.idea/**/dictionaries
.idea/**/shelf
# AWS User-specific
.idea/**/aws.xml
# Generated files
.idea/**/contentModel.xml
.DS_Store
# Sensitive or high-churn files
.idea/**/dataSources/
.idea/**/dataSources.ids
.idea/**/dataSources.local.xml
.idea/**/sqlDataSources.xml
.idea/**/dynamic.xml
.idea/**/uiDesigner.xml
.idea/**/dbnavigator.xml
# Gradle
.idea/**/gradle.xml
.idea/**/libraries
# File-based project format
*.iws
# IntelliJ
out/
# JIRA plugin
atlassian-ide-plugin.xml
# Python
*.py[cod]
*$py.class
# Distribution / packaging
.Python build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
*.manifest
*.spec
# Installer logs
pip-log.txt
pip-delete-this-directory.txt
# Unit test / coverage reports
htmlcov/
.tox/
.coverage
.coverage.*
.cache
.pytest_cache/
nosetests.xml
coverage.xml
*.cover
.hypothesis/
# Jupyter Notebook
.ipynb_checkpoints
# pyenv
.python-version
# celery
celerybeat-schedule.*
# SageMath parsed files
*.sage.py
# Environments
.env*
!.env.example*
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
# mkdocs documentation
/site
# mypy
.mypy_cache/
# Sublime Text
*.tmlanguage.cache
*.tmPreferences.cache
*.stTheme.cache
*.sublime-workspace
*.sublime-project
# sftp configuration file
sftp-config.json
# Package control specific files Package
Control.last-run
Control.ca-list
Control.ca-bundle
Control.system-ca-bundle
GitHub.sublime-settings
# Visual Studio Code
.vscode/*
!.vscode/settings.json
!.vscode/tasks.json
!.vscode/launch.json
!.vscode/extensions.json
.history -->

Selanjutnya, saya hubungkan repositori lokal dengan repositori GitHub yang telah dibuat sebelumnya, dengan perintah
<!-- git remote add origin https://github.com/pit135/PF_Shop.git -->
Perintah ini nambahin remote bernama origin yang menunjuk ke repositori GitHub saya, dengan nambahin remote ini, Git tau kemana harus mengirim kode kamu saat melakukan push. Terus, buat branch utama dengan nama master, trus jalanin perintah
<!-- git branch -M master -->
Trus pas udah, aku add, commit, dan push dari direktori repositori lokal ke git dengan cara pada umumnya/biasanya

g) Pembuatan Akun dan Deployment melalui PWS (Pacil Web Service)
=> Saya buka https://pbp.cs.ui.ac.id, trus login dengan SSO UI. Trus saya buat proyek baru dengan nama footballshoppp (gaboleh ada yg kapital). Trus kalo udah, pas akan keluar/muncul Project Credentials dan Project Command, nah yg project credential saya simpen di gdocs supaya ga ilang, karna ga akan ditampilin lagi tapi sangat amat penting.
Selanjutnya, saya ke bagian environs, trus isi raw editor dengan database yang dikasi di email tadi, atau yang ada di .env.prod.
Trus, di settings.py di proyek Django saya tambahin URL deployment PWS di bagian ALLOWED_HOSTS, URL deployment PWS formatnya <username-sso>-<nama proyek>.pbp.cs.ui.ac.id, jadi punya saya namanya petrus-wermasaubun-footballshoppp.pbp.cs.ui.ac.id.
<!-- ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<URL deployment PWS>"] -->

ini penting dilakukan supaya proyek Django bisa diakses melalui URL deployment PWS, trus saya lakukan git add, commit, dan push perubahan ini ke repositori GitHub seperti biasa, trus akan diminta username dan pw, nah saya masukin yang dari project credentials diawal. Trus kalo udah bisa pencet view peoject, brati projectnya dh kelar aman


<!-- ........................................................................................................................................................... -->


2. Membuat aplikasi dengan nama main pada proyek tersebut.
- Sebelum membuat aplikasi main, saya aktifkan dulu virtual environment yang udh dibuat sebelumnya dengan tujuan yang sudah saya sampaikan juga diata
- Setelah itu, saya jalankan kode dibawah agar muncul direktori baru dengan nama main, yang berisi struktur awal untuk aplikasi Django
python manage.py startapp main
- Selanjutnya, saya daftarin aplikasi main ke dalam proyek, yaitu dengan membuka berkas settings.py di dalam direktori proyek PF-Shop, tambahin  'main' ke dalam daftar aplikasi yang ada sebagai elemen paling terakhir
INSTALLED_APPS isinya daftar aplikasi yg dapat saya akses

<!-- INSTALLED_APPS = [
    ...,
    'main'
] -->

- Selanjutnya saya mengimplementasi template dasar, dimana membuat template yang berada di direktori templates yang berada di main. Template ini gunanya untuk menampilkan data program football shop saya.
- Langkah pertama adalah, membuat dan mengisi Berkas main.html. Apa itu HTML? HTML atau (Hypertext Markup Language) adalah bahasa penanda yang digunakan di halaman web untuk menafsirkan dan menulis teks, gambar dan bahan lainnya secara visual maupun suara. Selanjutnya, saya membuat direktori baru bernama templates di dalam direktori aplikasi main, trus buat berkas baru bernama main.html, isi dengan tamplate dibawah ( yg udh saya edit dengan data diri saya)

<!-- <h1>Football News</h1>

<h4>NPM: </h4>
<p>2406123456</p> 
<h4>Name: </h4>
<p>Pak Bepe</p> 
<h4>Class: </h4>
<p>PBP A</p>  -->

Seperti pengertiannya, yang saya lakukan diatas adalah hanya memeriksa tampilan dasar HTML dan belum terhubung dengan Django, jd saya buka dlu filenya di web, kalo udh sesuai penampakannya seperti yang saya mau, saya lanjutkan.


<!-- ........................................................................................................................................................... -->


3. Melakukan routing pada proyek agar dapat menjalankan aplikasi main
=> Setelah sudah memiliki aplikasi main di dalam proyek Django, supaya aplikasinya bisa dijalankan lewat browser saya perlu routing dulu, routing ini menghubungkan URL yang diakses client dengan view (fungsi/kelas) di aplikasi
langkah-langkahnya:
a) saya pastikan app main sudah dibuat & terdaftar
python manage.py startapp main
b) Setelah itu, di settings.py, saya tambahkan main ke INSTALLED_APPS:

<!-- INSTALLED_APPS = [
    ...
    'main', -->
buat file urls.py di dalam app main
dengan isi:
<!-- from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # URL root diarahkan ke fungsi index
] -->
c) di main/urls.py ke PF_Shop/urls.py
saya tambahkan di file PF_shop/urls.py:
<!-- from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),   # routing ke app main
] -->
d) Jalankan server
Setelah itu, harusnya udh aman dibuka webnya


<!-- ........................................................................................................................................................... -->


4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib 
Disini, saya mengubah berkas models.py yang ada di dalam direktori aplikasi main untuk mendefinisikan model baru

<!-- from django.db import models
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


   def __str__(self):
       return f"{self.name} - Rp{self.price:,}" -->

Penjelasan tiap code:
=> from django.db import models
mengimpor modul models dari framework Django, dan ini adalah modul inti yang saya butuhkan untuk mendefinisikan model, yaitu representasi tabel database saya

=> import uuid
Mengimpor modul uuid dari Python, modul ini untuk menghasilkan UUID (Universally Unique Identifier), untuk membuat ID utama yang unik secara universal

=> class Item(models.Model)
deklarasi kelas Python yang mendefinisikan model item. Kelas ini mewarisi dari models.Model, yang memberikannya semua fungsionalitas yang diperlukan untuk berinteraksi dengan database (misalnya, membuat, membaca, memperbarui, dan menghapus entri tabel)

=> CATEGORY_CHOICE
adalah sebuah daftar tuple yang digunakan untuk pilihan tetap untuk field category. Dengan cara ini, Anda memastikan bahwa nilai untuk kategori selalu konsisten dan terbatas pada pilihan yang ditentukan
'jersey': nilai aktual yang disimpan dalam database
'Jersey': teks yang akan ditampilkan di antarmuka administrasi Django

=>  id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
- id: berfungsi sebagai kunci utama (primary key) untuk setiap entri
- models.UUIDField: untuk menyimpan UUID
- primary_key=True: untuk kunci utama tabel
- default=uuid.uuid4: atur nilai default untuk field ini, setiap kali objek baru dibuat, UUID acak akan dihasilkan secara otomatis
- editable=False: mencegah nilai ini diubah melalui antarmuka administrasi

=> name = models.CharField(max_length=255)  
name: field ini menyimpan nama item
models.CharField: untuk string dengan panjang tetap
max_length=255: tetapkan panjang maksimum string, sebuah batasan yang umum untuk kolom teks pendek

=> price = models.IntegerField()       
price: field ini menyimpan harga item
models.IntegerField: untuk menyimpan bilangan bulat

=> stock = models.PositiveIntegerField(default=0)   
stock: field ini menyimpan jumlah stok item yang tersedia
models.PositiveIntegerField: Tipe field yang hanya menerima bilangan bulat non-negatif (0 atau lebih)
default=0: nilai default adalah 0 jika tidak ada nilai yang diberikan saat membuat objek.

=> brand = models.CharField(max_length=100)      
(misal: Adidas, Nike)
brand: field untuk menyimpan nama merek

=> size = models.CharField(max_length=50, blank=True)   
size: field untuk menyimpan ukuran item
blank=True: memungkinkan field ini kosong (misalnya, jika item tidak memiliki ukuran, seperti bola)

=> category = models.CharField(max_length=50 choices=CATEGORY_CHOICES)
category: field ini menyimpan kategori item
choices=CATEGORY_CHOICES: gunakan daftar tuple yang didefinisikan sebelumnya untuk membatasi pilihan yang valid

=> is_featured = models.BooleanField(default=False)   
is_featured: field boolean untuk menunjukkan apakah item ini ditampilkan di halaman utama atau promosi
models.BooleanField: tipe field yang menyimpan nilai True atau False
default=False: Nilai default adalah False

=> description = models.TextField() 
description: field untuk menyimpan deskripsi item
models.TextField: untuk string teks yang panjang, tanpa batasan panjang maksimum seperti CharField

=> thumbnail = models.URLField(blank=True, null=True) 
thumbnail: field untuk menyimpan URL gambar kecil (thumbnail).
models.URLField: untuk menyimpan URL yang valid
blank=True: memungkinkan field ini kosong di formulir
null=True: memungkinkan nilai database jadi NULL (tidak ada nilai)Blank hanya berlaku untuk formulir, sedangkan null berlaku untuk database

=> created_at = models.DateTimeField(auto_now_add=True)
created_at: field untuk mencatat waktu pembuatan objek
models.DateTimeField: menyimpan tanggal dan waktu
auto_now_add=True: otomatis mengisi waktu saat ini (ketika objek pertama kali dibuat) dan tidak dapat diubah setelah itu

<!-- =>  def __str__(self):
        return f"{self.name} - Rp{self.price:,}"
def __str__(self) -->
metode khusus Python yang mendefinisikan representasi string dari objek
Fungsi: mencetak objek Item (misalnya di konsol Django Shell atau antarmuka admin), ia akan menampilkan format yang mudah dibaca
<!-- f"{self.name} - Rp{self.price:,}": Ini adalah f-string yang memformat output -->
self.name: akses nama item
self.price: akses harga item dan menambahkan pemisah koma untuk ribuan (contoh: 1,000,000). Ini membuat harga lebih mudah dibaca


<!-- ........................................................................................................................................................... -->


5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu

Disini, saya mengintegrasikan komponen MVT, dengan impelemntasi code dibawah

<!-- from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Petrus Wermasaubun',
        'class': "PBP B",
  
    }

    return render(request, "main.html", context) -->

Penjelasan Kode:
<!-- from django.shortcuts import render -->
=> from django.shortcuts import render berguna untuk mengimpor fungsi render dari modul django
=> Fungsi render akan digunakan untuk render tampilan HTML dengan menggunakan data yang diberikan 
=> fungsi show_main di bawah impor:
kode di atas mendeklarasikan fungsi show_main, yang menerima parameter request, dimana fungsi ini akan mengatur permintaan HTTP dan mengembalikan tampilan yang sesuai
context adalah dictionary yang berisi data untuk dikirimkan ke tampilan, saat ini ada 2 data yang disertakan, yaitu:
name: data nama saya
class: data kelas saya
<!-- return render(request, "main.html", context)  -->
berguna untuk me-render tampilan main.html dengan menggunakan fungsi render, dimana fungsi render mengambil 2 argumen
=> request: adalah objek permintaan HTTP yang dikirim oleh pengguna
=> main.html: adalah nama berkas template yang akan digunakan untuk me-render tampilan
=> context: adalah dictionary yang berisi data yang akan diteruskan ke tampilan untuk digunakan dalam penampilan dinamis


<!-- ........................................................................................................................................................... -->


6. Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py.
=> Setelah membuat template dan mengonfigurasikannya pada view, melakukan routing agar aplikasi main dapat diakses oleh browser client
apa itu Routing di Django? routing adalah proses memetakan suatu URL ke sebuah view function atau class-based view (cara lain untuk membuat view namun menggunakan class guna mengorganisasi kode lebih baik) yang sudah kita definisikan, saat client mengakses URL tertentu, Django akan mencocokkan URL tersebut dengan pola yang ada di file urls.py, jika ada kecocokan, maka Django akan menjalankan view yang terkait dan mengembalikan response kepada client

=> Langkah 1:
saya mengonfigurasi Routing URL aplikasi main, dengan buat berkas urls.py di dalam direktori main
isi urls.py kode:
<!-- from django.urls import path
from main.views import show_main

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
] -->
penjelasan kode:
- file urls.py berisi konfigurasi routing untuk aplikasi main
- impor fungsi path dari modul django.urls untuk mendefinisikan pola URL
- impor fungsi show_main dari main.views yang akan dipanggil saat URL cocok dengan pola yang ditentukan
- app_name = 'main' digunakan untuk memberikan namespace unik pada URL dalam aplikasi, sehingga mudah dibedakan saat ada banyak aplikasi dan endpoint dalam proyek Django
- urlpatterns adalah list berisi objek URLPattern yang dihasilkan oleh fungsi path()
- di contoh ini, hanya ada satu route '' (root), yang akan memanggil view show_main
- agumen opsional name='show_main' memudahkan saya melakukan reverse URL menggunakan nama, bukan hardcoded string path

=> Langkah 2: 
mengonfigurasi Routing URL Proyek
Setelah itu saya melengkapi rute URL ke aplikasi main dengan menambahkan urls.py pada level proyek agar proyek dapat melakukan pemetaan ke rute URL pada aplikasi main
Berkas urls.py di dalam direktori proyek
Impor fungsi include dari django.urls
<!-- from django.urls import path, include -->
Selanjutnya, saya tambahkan rute URL berikut untuk mengarahkan ke tampilan main di dalam list urlpatterns
<!-- urlpatterns = [
    ...
    path('', include('main.urls')),
    ...
] -->
penjelasan kode:
- berkas urls.py proyek bertanggung jawab untuk mengatur rute URL level proyek
- fungsi include digunakan untuk mengimpor pola rute URL dari aplikasi lain (dalam hal ini dari aplikasi main) ke dalam berkas urls.py level proyek
- path URL '' akan diarahkan ke rute yang didefinisikan dalam berkas urls.py aplikasi main. Path URL dibiarkan berupa string kosong agar halaman aplikasi main dapat diakses secara langsung

Penjelasan diagram di tutorial:
- Client Request → Request dikirim oleh browser/HTTP client
- urls.py Level Projek → Semua request masuk pertama kali ke urls.py di project
- Jika pola cocok dengan include('main.urls'), request diteruskan ke urls.py aplikasi
- Jika tidak cocok, Django mengembalikan 404 Not Found
- urls.py Level Aplikasi → Pola URL di dalam aplikasi (main/urls.py) diproses
- View → Jika cocok, fungsi/class view dijalankan


<!-- ........................................................................................................................................................... -->


7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.
=> Pembuatan Akun dan Deployment melalui PWS (Pacil Web Service)
Saya buka https://pbp.cs.ui.ac.id, trus login dengan SSO UI. Trus saya buat proyek baru dengan nama footballshoppp (gaboleh ada yg kapital). Trus kalo udah, pas akan keluar/muncul Project Credentials dan Project Command, nah yg project credential saya simpen di gdocs supaya ga ilang, karna ga akan ditampilin lagi tapi sangat amat penting.
Selanjutnya, saya ke bagian environs, trus isi raw editor dengan database yang dikasi di email tadi, atau yang ada di .env.prod.
Trus, di settings.py di proyek Django saya tambahin URL deployment PWS di bagian ALLOWED_HOSTS, URL deployment PWS formatnya <username-sso>-<nama proyek>.pbp.cs.ui.ac.id, jadi punya saya namanya petrus-wermasaubun-footballshoppp.pbp.cs.ui.ac.id.
<!-- ALLOWED_HOSTS = ["localhost", "127.0.0.1", "<URL deployment PWS>"] -->
ini penting dilakukan supaya proyek Django bisa diakses melalui URL deployment PWS, trus saya lakukan git add, commit, dan push perubahan ini ke repositori GitHub seperti biasa, trus akan diminta username dan pw, nah saya masukin yang dari project credentials diawal. Trus kalo udah bisa pencet view peoject, brati projectnya dh kelar aman
Ya, intinya supaya teman2 saya bisa liat, tinggal saya share url project saya, atoga mereka harusnya bisa liat di readme ini, karena saya cantumin link url project saya dan direktori ini di git juga bersifat public, sapapun bisa liatt...


<!-- ........................................................................................................................................................... -->


8. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
![Bagan alur request-response Django](bagan.jpg)
Penjelasan Bagan:
a) Permintaan HTTP (HTTP Request)
Dimulai saat pengguna mengetik URL atau klik tautan di web, maka akan menghasilkan permintaan HTTP yang dikirim dari browser pengguna ke server web
b) URL Dispatcher (urls.py)
Django memiliki file urls.py yang berfungsi sebagai "peta jalan" untuk seluruh proyek, ketika permintaan HTTP tiba, Django akan melihat path dari permintaan tersebut (misalnya, /tentang/ atau /produk/123/, dll), lalu Django mencoba mencocokkan path ini dengan pola URL yang telah kita definisikan di urls.py, kalau ada pola yang cocok, Django akan meneruskan permintaan ke biew yang sesuai (yang ditentukan dalam pola URL), tapi kalo tidak ada pola yang cocok, Django akan mengembalikan respons HTTP 404 (Not Found)
c) View (views.py)
View adalah pusat dari logika aplikasi Django kita, view menerima objek permintaan HTTP (Request) yang berisi informasi tentang permintaan tersebut (misalnya, data formulir, cookie, header, dll), jika view perlu mengakses atau memanipulasi data, ia akan berinteraksi dengan model (models.py), view akan meminta data dari model (misalnya, "ambil semua produk yang harganya di bawah 100") atau menyimpan data baru ke dalamnya, lalu setelah view mendapatkan data yang dibutuhkan, ia akan memprosesnya (misalnya, menghitung total harga) dan mempersiapkannya untuk ditampilkan
d) Model (models.py)
Model adalah representasi objek dari tabel di database kita, kita bisa menganggapnya sebagai jembatan antara view dan database, view tidak berkomunikasi langsung dengan database menggunakan SQL melainkan view menggunakan metode-metode yang disediakan oleh model untuk membaca atau menulis data. Contohnya, Produk.objects.get(id=123) adalah perintah yang digunakan untuk mengambil data produk dengan ID tertentu, model berkomunikasi langsung dengan database yang sebenarnya, baik itu PostgreSQL, MySQL, atau SQLite, untuk menyimpan dan mengambil data
e) Template (<namafile>.html)
Setelah view selesai memproses data, ia akan mengambil file Template (biasanya berkas HTML), template ini berisi kerangka antarmuka pengguna. View akan menyuntikkan data yang sudah diproses ke dalam template, dengan cara ini, template menjadi dinamis dan dapat menampilkan data yang berbeda setiap kali dimuat
f) Respons HTTP (HTTP Response)
Setelah template diisi dengan data, view akan mengemasnya menjadi sebuah Respons HTTP yang lengkap, respons HTTP ini kemudian dikirim kembali ke server web, yang pada gilirannya mengirimkannya ke browser pengguna.
g) Halaman web ditampilkan
Terakhir, browser pengguna menerima Respons HTTP, memproses kode HTML, dan merender halaman web yang utuh, dinamis, dan interaktif yang dapat dilihat dan digunakan oleh pengguna.

intinya: request masuk ke urls.py yang mengarahkannya ke views.py, lalu view berinteraksi dengan models.py untuk mengelola data, dan kemudian menggunakan template HTML untuk menyajikan hasilnya kepada pengguna


<!-- ........................................................................................................................................................... -->


9. Jelaskan peran settings.py dalam proyek Django!
=> Dalam proyek Django, settings.py adalah file konfigurasi utama yang mengontrol semua aspek dari proyek web saya, simplenya atau bisa dianggap sebagai "otak" dari aplikasi Django saya
Setiap proyek Django pasti memiliki satu file settings.py yang berisi variabel-variabel global yang nentuin bagaimana aplikasi akan bekerja, mulai dari koneksi database sampai lokasi file statis


<!-- ........................................................................................................................................................... -->


10. Bagaimana cara kerja migrasi database di Django?
=> Migrasi database di Django adalah mekanisme untuk mengelola perubahan struktur database (misalnya membuat tabel baru, menambah kolom, menghapus kolom, atau mengubah tipe data) sesuai dengan perubahan yang saya buat di kode Python (dalam models.py).

Cara kerjanya:

=> membuat/mengubah model
dengan mendefinisikan struktur data di models.py.
Contoh:
<!-- from django.db import models
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2) -->

=> membuat file migrasi (makemigrations)
Django membaca perubahan pada models.py lalu menghasilkan file migrasi (misalnya 0001_initial.py) di folder migrations/
perintah:
<!-- python manage.py makemigrations -->
File migrasi ini berisi instruksi Python yang mewakili perubahan database, misalnya CreateModel, AddField, atau AlterField

=> menerapkan migrasi (migrate)
perintah:
<!-- python manage.py migrate -->
Django membaca file migrasi, lalu menerjemahkannya menjadi SQL statements (perintah SQL) yang dijalankan di database
misal:
<!-- CREATE TABLE product (
    id integer PRIMARY KEY AUTOINCREMENT,
    name varchar(100),
    price decimal(10,2)
); -->

=> catat migrasi di django_migrations
Django menyimpan riwayat migrasi yang sudah dijalankan di tabel khusus bernama django_migrations, supaya Django tau migrasi mana yang sudah diterapkan dan mana yang belum


<!-- ........................................................................................................................................................... -->


11. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
=> Alasan Django sering dijadikan framework permulaan dalam pembelajaran pengembangan perangkat lunak (khususnya web development) adalah karena sifat Django yang lengkap, terstruktur, dan edukatif
Berikut beberapa poin utamanya:

a) Baterai terpasang (Batteries Included)
Django menyediakan banyak fitur bawaan: ORM (Object Relational Mapping), autentikasi user, admin panel, form handling, middleware, templating system, dsb. Pemula tidak perlu menginstal banyak library tambahan untuk membangun aplikasi yang cukup kompleks

b) Struktur yang teratur (MVC/MVT)
Django memaksa kita menggunakan arsitektur MVT (Model–View–Template), sehingga sejak awal mahasiswa/pembelajar terbiasa dengan
models.py → urusan database
views.py → logika aplikasi
templates/ → tampilan HTML
Ini melatih pola pikir modular dan terstruktur, yang penting dalam software engineering

c) ORM yang mudah dipahami
Pemula bisa bekerja dengan database tanpa harus menulis SQL langsung
Contoh:
Product.objects.create(name="Sepatu", price=250000)
Django otomatis menerjemahkannya menjadi INSERT INTO product

d) Belajar konsep software engineering
Dengan Django, kita diperkenalkan pada:
Migrasi database (mirip versioning database), environments, version control (Git) terintegrasi dalam workflow, deployment (menjalankan aplikasi di server). Dimana bukan cuma soal ngoding, tapi juga soal engineering mindset

e) Komunitas besar & dokumentasi lengkap
Dokumentasi Django terkenal rapih, lengkap, dan ramah pemula, banyak tutorial dan forum diskusi, sehingga mahasiswa ga mudah stuck

f) Langsung melihat hasil

Cukup beberapa baris kode, pemula sudah bisa melihat aplikasi berjalan di browser, misalnya admin panel Django bisa langsung dipakai tanpa konfigurasi rumit, memberikan motivasi untuk belajar lebih


<!-- ........................................................................................................................................................... -->


12. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
=> Sangat ramah, baik, paling bersyukur adalah sangat membantu dengan gesit dan ramah, no judge2


<!-- ........................................................................................................................................................... -->

Repo: https://github.com/pit135/PF_Shop.git
Web: https://petrus-wermasaubun-footballshoppp.pbp.cs.ui.ac.id/


















================================================================= TUGAS 3 ==================================================================

1. Tambahkan 4 fungsi views baru untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
=> Tambahkan fungsi di main/views.py

a) Import yang diperlukan
Kenapa butuh ini?
- serializers untuk mengubah QuerySet → XML/JSON bawaan Django
- HttpResponse/JsonResponse untuk mengembalikan response dengan content-type yang tepat
- get_object_or_404 agar ID yang tidak ada langsung 404 (rapih)

# main/views.py
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import get_object_or_404
from .models import Item

b) View: XML (all)
Alasan: serializers.serialize("xml", queryset) menghasilkan string XML siap kirim
def show_xml(request):
    qs = Item.objects.all()
    xml_data = serializers.serialize("xml", qs)
    return HttpResponse(xml_data, content_type="application/xml")

c) View: JSON (all)
Alasan: sama kaya XML, tapi formatnya "json"
note: hasil serializers.serialize() udah berupa string JSON.=
Jadi pakai HttpResponse, jangan JsonResponse, supaya ga “double-encode”
def show_json(request):
    items = Item.objects.all()                      # ambil semua Item
    json_data = serializers.serialize("json", items)
    return HttpResponse(json_data, content_type="application/json")

d) View: XML by ID
Cara paling ringkas: ambil QuerySet terfilter (filter(pk=id)) → tetap QuerySet → langsung serialize
def show_xml_by_id(request, id):
    item_qs = Item.objects.filter(pk=id)                 # queryset (bisa kosong jika tidak ada)
    xml_data = serializers.serialize("xml", item_qs)
    return HttpResponse(xml_data, content_type="application/xml")


e) View: JSON by ID
Sama logikanya seperti XML by ID
def show_json_by_id(request, id):
    qs = Item.objects.filter(pk=id)
    if not qs.exists():
        return JsonResponse({"detail": "Not found"}, status=404)
    json_data = serializers.serialize("json", qs)
    return HttpResponse(json_data, content_type="application/json")




2. Membuat routing URL untuk masing-masing views yang telah ditambahkan pada poin 1.
- Tambahkan path url ke urlpatterns untuk akses fungsi yang udah diimpor kaya diatas, dan tanpa routing, fungsi ga bisa diakses dari browser/Postman

path("xml/", views.show_xml, name="show_xml"),        # ← endpoint XML
path('json/', views.show_json, name='show_json'),   # ← endpoint JSON
path("xml/<uuid:id>/", views.show_xml_by_id, name="show_xml_by_id"),
path("json/<uuid:id>/", views.show_json_by_id, name="show_json_by_id"),




3. Membuat halaman yang menampilkan data objek model yang memiliki tombol "Add" yang akan redirect ke halaman form, serta tombol "Detail" pada 
- Alasan dibuatnya adalah untuk menampilkan ringkasan item dan tombol Add memudahkan user menambah data, sedangkan tombol detail ke halaman khusus per item, dibuatnya di main/templates/main.html



- main/models.py —> “mendefinisikan struktur data” template akan menampilkan field‐field ini
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



- main/forms.py — “membuat form otomatis dari model, dipakai di halaman Add agar input user tervalidasi.
# main/forms.py
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "stock", "brand", "size",
                  "category", "is_featured", "description", "thumbnail"]



- main/views.py — “terima request, olah data, render template”, 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ItemForm
from .models import Item
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    items = Item.objects.all().order_by("-created_at")  # tampilkan terbaru dulu
    context = {
        'name': 'Petrus Wermasaubun',
        'class': "PBP B",
        'item_list': items,  # ganti dari news_list -> item_list
  
    }

    return render(request, "main.html", context)

def create_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            obj = form.save()
            messages.success(request, "Item berhasil ditambahkan.")
            return redirect("main:show_item", id=obj.pk)  # PRG: redirect ke detail
    else:
        form = ItemForm()
    return render(request, "add_item.html", {"form": form})

def show_item(request, id):
    item = get_object_or_404(Item, pk=id)  # id = UUID
    return render(request, "item_detail.html", {"item": item})

def show_xml(request):
    items = Item.objects.all()                       # ambil semua Item
    xml_data = serializers.serialize("xml", items)   # serialize ke XML
    return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    items = Item.objects.all()                      # ambil semua Item
    json_data = serializers.serialize("json", items)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, id):
    item_qs = Item.objects.filter(pk=id)                 # queryset (bisa kosong jika tidak ada)
    xml_data = serializers.serialize("xml", item_qs)
    return HttpResponse(xml_data, content_type="application/xml")

def show_json_by_id(request, id):
    item = Item.objects.get(pk=id)                       # akan error 404 jika id tidak ada
    json_data = serializers.serialize("json", [item])    # bungkus list untuk serialize satu objek
    return HttpResponse(json_data, content_type="application/json")



- main/templates/base.html — “kerangka HTML induk”

<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="utf-8">
  <title>PF Shop</title>
</head>
<body>
  {% block content %}{% endblock %}
</body>
</html>
Supaya halaman lain tinggal {% extends 'base.html' %}



- main/templates/main.html — “menampilkan semua item + tombol navigasi”

{% extends 'base.html' %}
{% load humanize %}
{% block content %}

<h1>PF Shop</h1>

<h5>Name:</h5>
<p>{{ name }}</p>

<h5>Class:</h5>
<p>{{ class }}</p>

<a href="{% url 'main:create_item' %}">
  <button>+ Add Item</button>
</a>

<hr>

{% for item in item_list %}
  <div>
    <h2><a href="{% url 'main:show_item' item.id %}">{{ item.name }}</a></h2>

    <div class="meta">
      <p><strong>Category:</strong> {{ item.get_category_display }}</p>
      {% if item.is_featured %}<p><strong>Featured:</strong> Yes</p>{% endif %}
      {% if item.size %}<p><strong>Size:</strong> {{ item.size }}</p>{% endif %}
      <p><strong>Brand:</strong> {{ item.brand }}</p>
      <p><strong>Price:</strong> Rp{{ item.price|intcomma }}</p>
      <p><strong>Stock:</strong> {{ item.stock }}</p>
    </div>

    {% if item.thumbnail %}
      <img src="{{ item.thumbnail }}" alt="thumbnail" width="150" height="100"><br />
    {% endif %}

    <p>{{ item.description|truncatewords:25 }}...</p>
    <p><a href="{% url 'main:show_item' item.id %}"><button>Detail</button></a></p>
  </div>
  <hr>
{% empty %}
  <p>Belum ada data item.</p>
{% endfor %}

{% endblock %}


-> {% url 'main:create_item' %} → tombol Add menuju form.
-> {% url 'main:show_item' item.id %} → tombol Detail menuju halaman detail item.
-> {{ item_list }} → datang dari view show_main (jangan salah pakai nama variabel).
-> |intcomma → formatting angka (aktifkan django.contrib.humanize di INSTALLED_APPS).
 
 
 
- main/templates/add_item.html — “form tambah item”

{% extends 'base.html' %}
{% block content %}
<h1>Add Item</h1>

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Add Item</button>
  <a href="{% url 'main:show_main' %}">Cancel</a>
</form>
{% endblock %}


-> {% csrf_token %} → wajib agar POST aman (mencegah CSRF)
-> {{ form.as_p }} → render field yang didefinisikan di ItemForm
 
 
=> Alur pakai (cek hasil)
- Buka / → lihat list (main.html), klik + Add Item.
- Isi form → Submit → diarahkan ke detail (/item/<id>/).
- Klik “Back to list” → item akan muncul di list.
 
 

 
 
4. setiap data objek model yang akan menampilkan halaman detail objek
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

- main/urls.py, id di path ini nanti diisi item.id dari database
- main/views.py, ambil item berdasarkan id. Kalau tidak ada, otomatis 404 (rapi)
- Di template list kamu (mis. main/templates/main.html), di dalam loop, Kuncinya: {% url 'main:show_item' item.id %} mengarah ke route di langkah #1
- main/templates/item_detail.html





5. Membuat halaman form untuk menambahkan objek model pada app sebelumnya
# main/forms.py
from django.forms import ModelForm
from .models import Item

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["name", "price", "stock", "brand", "size",
                  "category", "is_featured", "description", "thumbnail"]

Kenapa perlu csrf_token?
Untuk mencegah CSRF (lihat penjelasan di Q&A). Tanpa token, request POST dari situs lain bisa “menunggangi” sesi user yang login.

# main/templates/add_item.html
{% extends 'base.html' %}
{% block content %}
<h1>Add Item</h1>

<form method="post">
  {% csrf_token %}
  {{ form.as_p }}
  <button type="submit">Add Item</button>
  <a href="{% url 'main:show_main' %}">Cancel</a>
</form>
{% endblock %}





6. Membuat halaman yang menampilkan detail dari setiap data objek model
{% extends 'base.html' %}
{% load humanize %}
{% block content %}
<p><a href="{% url 'main:show_main' %}"><button>← Back to Item List</button></a></p>

<h1>{{ item.name }}</h1>
<div class="meta">
  <p><strong>Category:</strong> {{ item.get_category_display }}</p>
  {% if item.is_featured %}<p><strong>Featured:</strong> Yes</p>{% endif %}
  {% if item.size %}<p><strong>Size:</strong> {{ item.size }}</p>{% endif %}
  <p><strong>Brand:</strong> {{ item.brand }}</p>
  <p><strong>Price:</strong> Rp{{ item.price }}</p>
  <p><strong>Stock:</strong> {{ item.stock }}</p>
  <p><strong>Created:</strong> <i>{{ item.created_at|date:"d M Y, H:i" }}</i></p>
</div>

{% if item.thumbnail %}
  <img src="{{ item.thumbnail }}" alt="Item thumbnail" width="300">
  <br><br>
{% endif %}

<div>
  {{ item.description|linebreaks }}
</div>
{% endblock content %}

Supaya halaman itu “bisa didapatkan/ditampilkan” di browser, kamu perlu melengkapi alur MVT Django: URL → View → Query ke DB → Render template. Berikut langkahnya, lengkap “kode mana untuk apa”.

-> Routing URL (mengatur alamat halaman detail)
File: main/urls.py
Tujuan: ketika user membuka /item/1/, Django memanggil fungsi view yang tepat
item/<int:id>/ artinya URL butuh angka sebagai id
name="show_item" dipakai di template untuk membuat link dengan {% url 'main:show_item' item.id %}
Pastikan project/urls.py sudah include("main.urls")

- View detail (mengambil data & render template)
File: main/views.py
Tujuan: ambil Item berdasar id, kirim ke template sebagai variabel item (yang kamu pakai di template)
get_object_or_404 otomatis kirim 404 bila id tidak ditemukan (rapi & aman)
Nama key di context harus item, karena template kamu memakai {{ item.* }}

- Template detail 
File: main/templates/item_detail.html
Tujuan: menampilkan data yang dikirim dari view
{{ item.get_category_display }} otomatis menampilkan label dari field choices
|date:"d M Y, H:i" memformat tanggal created_at
|linebreaks mengubah newline menjadi <p>/<br>
Kamu bisa tambah |intcomma untuk harga/angka agar lebih enak dibaca

- Link “Detail” dari halaman list (supaya bisa “masuk” ke detail)
File: main/templates/main.html (di dalam loop)
{% url 'main:show_item' item.id %} membentuk URL /item/<id>/ sesuai route di langkah 1





7.  Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
- Decoupling (pisah front-end & back-end)
Tanpa data delivery, UI harus “tahu” struktur database. Dengan API, front-end (web/mobile) cukup minta data lewat kontrak yang stabil → lebih mudah ganti UI/teknologi tanpa menyentuh logika bisnis & DB.
- Interoperabilitas lintas klien
Satu sumber data bisa dipakai banyak klien: web, Android, iOS, layanan pihak ketiga, bahkan CLI/automasi. Format standar (JSON/XML) memudahkan integrasi.
- Keamanan: jangan expose DB
Klien tidak pernah langsung mengakses database. API jadi gerbang bertingkat: autentikasi, otorisasi (role/permission), rate-limit, input validation, audit logging. Risiko SQL injection & data leakage jauh turun.
- Skalabilitas & kinerja
API memungkinkan caching (HTTP cache, CDN), pagination, filtering, partial fields (hanya kirim yang perlu). Ini menghemat bandwidth & beban server saat traffic besar.
- Konsistensi logika bisnis
Aturan bisnis (diskon, stok, validasi) tinggal ditulis satu kali di back-end. Semua klien otomatis konsisten karena mengonsumsi endpoint yang sama.
- Kontrak data yang jelas (schema)
Dengan spesifikasi (OpenAPI/Swagger, JSON Schema), tim punya kontrak eksplisit: tipe data, field wajib, error codes, versi API. Ini mengurangi salah paham antartim.
- Evolusi & versioning 
API bisa berkembang (v1 → v2) tanpa mematikan klien lama. Backward compatibility dikelola lewat versioning & feature flags.
- Observabilitas & reliabilitas
Layer API memudahkan monitoring (latensi, error rate), tracing, retry, circuit breaker. Operasional jadi terukur & bisa ditingkatkan.
- Kepatuhan & privasi
Lebih mudah menerapkan data minimization (hanya field perlu), masking PII, serta enforcement kebijakan (GDPR/PDPA) dibanding membiarkan klien mengakses tabel mentah.
- Arsitektur modern (microservices & event-driven)
Service lain bisa mengonsumsi data via REST/GraphQL atau webhook/queue (event delivery). Ini dasar integrasi antar-service.




8.  Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Saya hampir selalu milih JSON buat urusan API
Kenapa?
- Ringkas & ngebut: ukuran payload kecil, jadi hemat bandwidth dan lebih responsif
- Gampang di-oprek di front-end: tinggal JSON.parse() di JS/TS, beres
- Strukturnya natural: objek & array langsung nyambung ke tipe data di Python/Java/Go
- Ekosistemnya rame: OpenAPI/Swagger, JSON Schema, mock server, linting—semua ready
- XML tetap ada tempatnya, tapi lebih niche:
- Kalau ketemu sistem legacy (mis. SOAP) atau standar/regulasi yang wajib XML
- Kalau butuh dokumen yang kompleks: namespace, atribut, mixed content, validasi super ketat via XSD
- Kalau konteksnya app (PF Shop):
- JSON jadi format utama biar web/mobile gampang konsumsi
- XML tetap disediain buat kompatibilitas/tugas penilaian, tapi bukan default




9. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Apa itu is_valid()?
- Method pada Django Form/ModelForm yang:
- Menjalankan semua validasi
- Mengisi form.cleaned_data (data yang sudah dibersihkan & dikonversi tipe)
- Mengisi form.errors kalau ada masalah
- Mengembalikan True kalau tidak ada error, selain itu False
- Catatan: Form harus “bound” (dibuat dengan data, mis. request.POST) supaya bisa divalidasi. Form yang tidak diisi (unbound) akan is_valid() == False

Apa saja yang divalidasi?
- Ketika kamu memanggil form.is_valid() Django melakukan:
- Validasi level field: tipe data, required, max_length, choices, validators
- clean_<field>() (jika kamu definisikan) untuk kustom 1 field
- clean() (jika kamu definisikan) untuk aturan lintas-field (mis. start_date < end_date)
- Model-level (khusus ModelForm): constraint model seperti unique, UniqueConstraint/unique_together dan validator model lain. Ini mencegah tabrakan unik di DB

Hasilnya:
- form.cleaned_data berisi nilai yang sudah “bersih” (mis. string → int, strip spasi, dsb.)
- form.errors / form.non_field_errors() berisi pesan error yang siap ditampilkan ke user
- Kenapa kita butuh is_valid()?
- Keamanan: mencegah input berbahaya/format tidak sah masuk ke sistem
- Integritas data: menghindari IntegrityError (mis. field unik dobel) dan data rusak
- UX yang baik: pesan error muncul rapi di form (bukan error 500)
- Normalisasi data: konversi tipe & pembersihan nilai sebelum dipakai/simpan
- Konsistensi aturan bisnis: semua klien (web/mobile) lewat jalur validasi yang sama





10.  Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?

Singkatnya: {% csrf_token %} itu tameng utama supaya form kamu nggak bisa dipakai orang lain buat “klik” atas nama user tanpa sepengetahuan mereka (CSRF)

CSRF itu apa?
Cross-Site Request Forgery = serangan di mana penyerang bikin browser korban mengirim request sah (lengkap dengan cookie sesi/login) ke situsmu, tanpa korban sadar
Contoh: user sedang login di situsmu, lalu membuka situs jahat → situs jahat itu menyelipkan form auto-submit ke /transfer/, dan browser otomatis mengirim cookie session korban ke situsmu

Kenapa perlu csrf_token?
Karena browser otomatis bawa cookie (sessionid) saat mengakses domainmu. Tanpa mekanisme tambahan, server nggak bisa bedain:
request dari halaman kamu sendiri (legit), vs
request dari situs lain (jahat) yang “nebeng” cookie user.
csrf_token menambahkan rahasia satu-kali-pakai (token) di halaman/form milikmu. Django:
menaruh token di cookie csrftoken,
minta token yang sama dikirim kembali di body form ({% csrf_token %}) atau header X-CSRFToken (AJAX),
mencocokkan keduanya + (untuk HTTPS) validasi Origin/Referer.
Kalau nggak cocok → 403 Forbidden
Ini disebut pola double submit cookie + origin check

Kalau nggak pakai csrf_token, apa yang terjadi?
Dua kemungkinan:
- CSRF middleware aktif (default di Django)
Request POST/PUT/PATCH/DELETE dari form tanpa token → ditolak 403
Gejala di dev: “CSRF verification failed. Request aborted.”
CSRF middleware dimatikan / view di-@csrf_exempt
- Aplikasi kamu rentan CSRF. Penyerang bisa:
menambah item / mengubah profil / ganti email / ubah password (kalau endpoint tidak minta password lama)
melakukan transaksi (top-up, transfer, order barang)
aksi admin jika user yang login adalah admin
Semua terjadi tanpa klik sadar dari user—cukup bikin halaman jahat yang auto-submt

4) Skema serangan (contoh konkret)
Situs jahat menaruh HTML ini:
<form action="https://app-kamu.com/add/" method="POST">
  <input type="hidden" name="name" value="Item dari hacker">
  <input type="hidden" name="price" value="9999999">
</form>
<script>document.forms[0].submit()</script>
Korban sedang login di app-kamu.com, lalu buka halaman ini. Browser korban:
mengirim POST ke app-kamu.com/add/
membawa cookie session korban
Jika tidak ada verifikasi CSRF, server menganggap ini request sah dari user → data berubah.
Catatan: Kebijakan cookie modern SameSite=Lax memang membantu, tapi bukan pengganti CSRF token (masih ada kasus yang lolos, edge cases, subdomain, metode/flow tertentu). Jangan mengandalkan ini saja.


11. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
=> SANGAT AMAT BAIK DAN HELPFULLLL.......
MAKASIII BANYAK BANYAK KAAA...




12.  Mengakses keempat URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md

![json postman](json.jpg)
![xml postman](xml.jpg)
![json postman with news id](jsonwnewsid.jpg)
![xml postman with news id](xmlwnewsid.jpg)
