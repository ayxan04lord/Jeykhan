from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.core.models import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(ModelAdmin):
    list_display = ["name", "location", "cuisine_type", "is_active", "order"]
    list_filter = ["is_active", "cuisine_type"]
    search_fields = ["name", "description", "location"]
    list_editable = ["is_active", "order"]
    ordering = ["order", "name"]
    prepopulated_fields = {"slug": ("name",)}

    fieldsets = (
        ("Əsas Məlumatlar", {
            "fields": ("name", "slug", "short_description", "description", "cuisine_type", "location")
        }),
        ("Əlaqə və Linklər", {
            "fields": ("phone_number", "website_url", "instagram_url")
        }),
        ("Şəkillər", {
            "fields": ("logo", "cover_image"),
            "classes": ("collapse",),
        }),
        ("Göstəriş", {
            "fields": ("is_active", "order"),
            "classes": ("collapse",),
        }),
    )
