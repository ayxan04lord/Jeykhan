from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator, URLValidator


class Service(models.Model):
    """Model for services offered in restaurant management and music training"""

    CATEGORY_CHOICES = [
        ("restaurant", "Restaurant Management"),
        ("music", "Music Training"),
    ]

    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3, "Title must be at least 3 characters long")],
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(
        validators=[
            MinLengthValidator(10, "Description must be at least 10 characters long")
        ]
    )
    icon = models.CharField(max_length=50, help_text="CSS class for icon display")
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(
        default=0, help_text="Display order (lower numbers appear first)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "title"]
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"


class Experience(models.Model):
    """Model for professional experience in different fields"""

    CATEGORY_CHOICES = [
        ("restaurant", "Restaurant Management"),
        ("music", "Music Training"),
    ]

    title = models.CharField(
        max_length=100,
        validators=[MinLengthValidator(3, "Title must be at least 3 characters long")],
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(
        validators=[
            MinLengthValidator(10, "Description must be at least 10 characters long")
        ]
    )
    years_experience = models.IntegerField(
        help_text="Number of years of experience in this area"
    )
    is_featured = models.BooleanField(
        default=False, help_text="Display on homepage highlights"
    )
    order = models.IntegerField(
        default=0, help_text="Display order (lower numbers appear first)"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-years_experience", "title"]
        verbose_name = "Experience"
        verbose_name_plural = "Experiences"

    def __str__(self):
        return f"{self.title} - {self.years_experience} years ({self.get_category_display()})"


class ContactInfo(models.Model):
    """Model for contact information"""

    phone_validator = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
    )

    phone_number = models.CharField(
        max_length=20,
        validators=[phone_validator],
        help_text="Primary phone number for contact",
    )
    email = models.EmailField(blank=True, help_text="Optional email address")
    address = models.TextField(blank=True, help_text="Optional physical address")
    is_active = models.BooleanField(
        default=True, help_text="Use this contact information"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-is_active", "-created_at"]
        verbose_name = "Contact Information"
        verbose_name_plural = "Contact Information"

    def __str__(self):
        return f"Contact: {self.phone_number}" + (
            f" ({self.email})" if self.email else ""
        )


class Restaurant(models.Model):
    """Model for restaurants managed by Ceyhan Nur"""

    name = models.CharField(max_length=150, verbose_name="Restoranın adı")
    slug = models.SlugField(max_length=150, unique=True, verbose_name="Slug")
    description = models.TextField(verbose_name="Haqqında")
    short_description = models.CharField(
        max_length=250,
        verbose_name="Qısa məlumat",
        help_text="Kartda göstəriləcək qısa məlumat",
    )
    cuisine_type = models.CharField(
        max_length=100,
        blank=True,
        verbose_name="Mətbəx növü",
        help_text="Məs: Azərbaycan, Avropa, Fast Food",
    )
    location = models.CharField(
        max_length=200, blank=True, verbose_name="Ünvan/Şəhər"
    )
    phone_number = models.CharField(
        max_length=30, blank=True, verbose_name="Rezervasiya nömrəsi"
    )
    website_url = models.URLField(
        blank=True,
        verbose_name="Rəsmi sayt",
        help_text="Rəsmi sayt varsa daxil edin",
    )
    instagram_url = models.URLField(
        blank=True,
        verbose_name="Instagram",
        help_text="Rəsmi sayt yoxdursa Instagram linki",
    )
    logo = models.ImageField(
        upload_to="restaurants/logos/",
        blank=True,
        null=True,
        verbose_name="Logo",
    )
    cover_image = models.ImageField(
        upload_to="restaurants/covers/",
        blank=True,
        null=True,
        verbose_name="Üz şəkli",
    )
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(
        default=0,
        verbose_name="Sıra",
        help_text="Kiçik rəqəm əvvəl göstərilir",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "name"]
        verbose_name = "Restoran"
        verbose_name_plural = "Restoranlar"

    def __str__(self):
        return self.name

    @property
    def external_link(self):
        """Returns website URL if exists, otherwise Instagram URL"""
        return self.website_url or self.instagram_url

    @property
    def reservation_phone(self):
        """Returns restaurant-specific phone or falls back to contact info"""
        return self.phone_number


class TVShow(models.Model):
    """Model for TV shows and culinary programs Ceyhan Nur appeared in"""

    SHOW_TYPE_CHOICES = [
        ("competition", "Müsabiqə"),
        ("educational", "Təhsil/Tədris"),
        ("entertainment", "Əyləncə"),
        ("documentary", "Sənədli"),
    ]

    title = models.CharField(max_length=200, verbose_name="Verlişin adı")
    channel = models.CharField(
        max_length=100, blank=True, verbose_name="Kanal/Platforma"
    )
    country = models.CharField(
        max_length=100, blank=True, verbose_name="Ölkə", help_text="Məs: Azərbaycan, Rusiya"
    )
    show_type = models.CharField(
        max_length=50,
        choices=SHOW_TYPE_CHOICES,
        default="competition",
        verbose_name="Növ",
    )
    description = models.TextField(verbose_name="Haqqında")
    year = models.IntegerField(
        blank=True, null=True, verbose_name="İl", help_text="İştirak ili"
    )
    result = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Nəticə/Yer",
        help_text="Məs: Qalib, 2-ci yer, İştirakçı",
    )
    poster = models.ImageField(
        upload_to="projects/shows/",
        blank=True,
        null=True,
        verbose_name="Poster/Şəkil",
    )
    youtube_url = models.URLField(
        blank=True, verbose_name="YouTube linki"
    )
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    is_featured = models.BooleanField(
        default=False, verbose_name="Öne çıxan", help_text="Ana səhifədə göstər"
    )
    order = models.IntegerField(default=0, verbose_name="Sıra")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-year"]
        verbose_name = "Veriliş"
        verbose_name_plural = "Verilişlər"

    def __str__(self):
        return f"{self.title} ({self.year or 'tarix yoxdur'})"


class Product(models.Model):
    """Model for products created/launched by Ceyhan Nur (e.g. mestixumarcay)"""

    name = models.CharField(max_length=200, verbose_name="Məhsulun adı")
    tagline = models.CharField(
        max_length=250, blank=True, verbose_name="Slogan/Qısa cümlə"
    )
    description = models.TextField(verbose_name="Haqqında")
    launch_year = models.IntegerField(
        blank=True, null=True, verbose_name="Buraxılış ili"
    )
    website_url = models.URLField(blank=True, verbose_name="Sayt")
    instagram_url = models.URLField(blank=True, verbose_name="Instagram")
    image = models.ImageField(
        upload_to="projects/products/",
        blank=True,
        null=True,
        verbose_name="Şəkil",
    )
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    is_featured = models.BooleanField(
        default=False, verbose_name="Öne çıxan", help_text="Ana səhifədə göstər"
    )
    order = models.IntegerField(default=0, verbose_name="Sıra")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-launch_year"]
        verbose_name = "Məhsul"
        verbose_name_plural = "Məhsullar"

    def __str__(self):
        return self.name


class Achievement(models.Model):
    """Model for certificates, medals, diplomas and awards"""

    ACHIEVEMENT_TYPE_CHOICES = [
        ("gold_medal", "Qızıl Medal"),
        ("silver_medal", "Gümüş Medal"),
        ("bronze_medal", "Bürünc Medal"),
        ("certificate", "Sertifikat"),
        ("diploma", "Diploma"),
        ("award", "Mükafat"),
        ("title", "Fəxri Ad"),
    ]

    title = models.CharField(max_length=200, verbose_name="Adı")
    achievement_type = models.CharField(
        max_length=50,
        choices=ACHIEVEMENT_TYPE_CHOICES,
        verbose_name="Növü",
    )
    issuer = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Verən qurum",
        help_text="Məs: Azərbaycan Kulinariya Federasiyası",
    )
    description = models.TextField(blank=True, verbose_name="Ətraflı məlumat")
    year = models.IntegerField(
        blank=True, null=True, verbose_name="İl"
    )
    competition_name = models.CharField(
        max_length=200,
        blank=True,
        verbose_name="Müsabiqə/Yarışma adı",
    )
    image = models.ImageField(
        upload_to="achievements/",
        blank=True,
        null=True,
        verbose_name="Şəkil/Skan",
    )
    is_active = models.BooleanField(default=True, verbose_name="Aktiv")
    order = models.IntegerField(default=0, verbose_name="Sıra")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-year", "title"]
        verbose_name = "Nailiyyət"
        verbose_name_plural = "Nailiyyətlər"

    def __str__(self):
        return f"{self.get_achievement_type_display()} — {self.title} ({self.year or '—'})"

    @property
    def medal_icon(self):
        icons = {
            "gold_medal": "🥇",
            "silver_medal": "🥈",
            "bronze_medal": "🥉",
            "certificate": "📜",
            "diploma": "🎓",
            "award": "🏆",
            "title": "⭐",
        }
        return icons.get(self.achievement_type, "🏅")
