from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Service, Experience, ContactInfo


@admin.register(Service)
class ServiceAdmin(ModelAdmin):
    """Admin configuration for Service model"""

    list_display = ["title", "category", "is_active", "order", "created_at"]
    list_filter = ["category", "is_active", "created_at"]
    search_fields = ["title", "description"]
    list_editable = ["is_active", "order"]
    ordering = ["order", "title"]

    fieldsets = (
        ("Əsas Məlumatlar", {"fields": ("title", "category", "description", "icon")}),
        (
            "Göstəriş Parametrləri",
            {"fields": ("is_active", "order"), "classes": ("collapse",)},
        ),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()


@admin.register(Experience)
class ExperienceAdmin(ModelAdmin):
    """Admin configuration for Experience model"""

    list_display = [
        "title",
        "category",
        "years_experience",
        "is_featured",
        "order",
        "created_at",
    ]
    list_filter = ["category", "is_featured", "created_at"]
    search_fields = ["title", "description"]
    list_editable = ["is_featured", "order"]
    ordering = ["order", "-years_experience"]

    fieldsets = (
        (
            "Əsas Məlumatlar",
            {"fields": ("title", "category", "description", "years_experience")},
        ),
        (
            "Göstəriş Parametrləri",
            {"fields": ("is_featured", "order"), "classes": ("collapse",)},
        ),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()


@admin.register(ContactInfo)
class ContactInfoAdmin(ModelAdmin):
    """Admin configuration for ContactInfo model"""

    list_display = ["phone_number", "email", "is_active", "created_at"]
    list_filter = ["is_active", "created_at"]
    search_fields = ["phone_number", "email"]
    list_editable = ["is_active"]
    ordering = ["-is_active", "-created_at"]

    fieldsets = (
        ("Əlaqə Təfərrüatları", {"fields": ("phone_number", "email", "address")}),
        ("Parametrlər", {"fields": ("is_active",), "classes": ("collapse",)}),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).select_related()

    def has_add_permission(self, request):
        # Eyni vaxtda yalnız bir aktiv əlaqə məlumatına icazə ver
        if ContactInfo.objects.filter(is_active=True).exists():
            return False
        return super().has_add_permission(request)
