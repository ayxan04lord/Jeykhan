# Ceyhan Nur — Şəxsi Portfolio Saytı

Azərbaycanın tanınmış restoran idarəçisi **Ceyhan Nur**un şəxsi portfolio saytı. Django əsaslı, tam CMS dəstəkli, müasir dizaynlı veb layihə.

---

## 👤 Sayt Kimi Haqqındadır?

**Ceyhan Nur** — Azərbaycanın Masallı şəhərinin məşhur restoran idarəçisi. İdarə etdiyi məkanlar:

| Restoran | Növ |
|---|---|
| Masallı Hotel Restoran | Otel restoranı |
| Masallı Hotel İsti Su | Spa & Restoran |
| Kəndli Organic Fastfood | Organik Fast Food |
| Kafe O | Şəhər kafesi |
| Terras Masallı Pub Lounge | Pub & Lounge |

**Nailiyyətlər:** 28 Qızıl Medal · 5 TV Verilişi · mestixumarcay brendi

---

## 🗂️ Səhifələr

| URL | Səhifə | Məzmun |
|---|---|---|
| `/` | Ana Səhifə | Hero, xidmətlər, təcrübə |
| `/haqqimizda/` | Haqqımda | Peşəkar keçmiş, bacarıqlar |
| `/restoranlar/` | Restoranlar | 5 restoran, rezervasiya düymələri |
| `/layiheler/` | Layihələr | TV verilişləri, mestixumarcay |
| `/nailiyyetler/` | Nailiyyətlər | 28 qızıl medal, sertifikatlar |
| `/xidmetler/` | Xidmətlər | Kulinariya & musiqi xidmətləri |
| `/admin/` | Admin Panel | CMS idarəetmə paneli |

---

## 🛠️ Texnologiyalar

- **Backend:** Django 4.2
- **Verilənlər bazası:** MySQL 8.4
- **Admin:** django-unfold (müasir UI)
- **Frontend:** Vanilla CSS + JS, Poppins, Font Awesome 6
- **Media:** Pillow
- **Env:** python-dotenv

---

## ⚡ Quraşdırma

### Tələblər
- Python 3.10+
- MySQL 8+
- pip

### Addımlar

```bash
# 1. Layihəni klonla
git clone <repo-url>
cd jeykhan

# 2. Virtual mühit yarat
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Linux/Mac

# 3. Asılılıqları quraşdır
pip install -r requirements.txt

# 4. .env faylını yarat
copy .env.example .env       # Windows
# cp .env.example .env       # Linux/Mac
# .env içindəki MySQL məlumatlarını doldur

# 5. MySQL-də database yarat
mysql -u root -p
CREATE DATABASE jeykhan_portfolio CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
EXIT;

# 6. Migration-ları tətbiq et
python manage.py migrate

# 7. Superuser yarat
python manage.py createsuperuser

# 8. Serveri işə sal
python manage.py runserver
```

Sayt: `http://127.0.0.1:8000`  
Admin: `http://127.0.0.1:8000/admin`

---

## 🔧 .env Nümunəsi

`.env` faylında aşağıdakı dəyişənlər lazımdır:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here

DB_ENGINE=django.db.backends.mysql
DB_NAME=jeykhan_portfolio
DB_USER=root
DB_PASSWORD=your-mysql-password
DB_HOST=127.0.0.1
DB_PORT=3306

LANGUAGE_CODE=az-az
TIME_ZONE=Asia/Baku
```

---

## 📁 Layihə Strukturu

```
jeykhan/
├── apps/
│   ├── core/           # Mərkəzi modellər (bütün app-lar buradan import edir)
│   ├── home/           # Ana səhifə
│   ├── about/          # Haqqımda
│   ├── restaurants/    # Restoranlar
│   ├── projects/       # TV verilişləri & məhsullar
│   ├── achievements/   # Medallar & sertifikatlar
│   └── services/       # Xidmətlər
├── config/
│   ├── settings.py
│   └── urls.py
├── templates/
│   ├── layouts/base.html
│   ├── includes/
│   └── pages/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── .env
├── requirements.txt
└── manage.py
```

---

## 🗄️ Verilənlər Bazası Modelləri

| Model | App | Məqsəd |
|---|---|---|
| `Service` | core | Kulinariya & musiqi xidmətləri |
| `Experience` | core | Peşəkar təcrübə |
| `ContactInfo` | core | Əlaqə məlumatları |
| `Restaurant` | core | Restoran məlumatları |
| `TVShow` | core | TV verilişləri |
| `Product` | core | Brendlər (mestixumarcay) |
| `Achievement` | core | Medal, sertifikat, diploma |

---

## 👨‍💻 Hazırladı

Bu layihə Ceyhan Nurun şəxsi sifarişi ilə hazırlanmışdır.
