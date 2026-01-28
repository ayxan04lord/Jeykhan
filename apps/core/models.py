from django.db import models
from django.core.validators import MinLengthValidator, RegexValidator


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
