from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.core.models import TVShow, Product


@admin.register(TVShow)
class TVShowAdmin(ModelAdmin):
    list_display = ["title", "channel", "country", "year", "result", "is_featured", "is_active", "order"]
    list_filter = ["show_type", "country", "is_featured", "is_active"]
    search_fields = ["title", "channel", "description"]
    list_editable = ["is_featured", "is_active", "order"]
    ordering = ["order", "-year"]

    fieldsets = (
        ("Veriliş Məlumatları", {
            "fields": ("title", "channel", "country", "show_type", "year", "result")
        }),
        ("Məzmun", {
            "fields": ("description", "poster", "youtube_url")
        }),
        ("Göstəriş", {
            "fields": ("is_active", "is_featured", "order"),
            "classes": ("collapse",),
        }),
    )


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    list_display = ["name", "tagline", "launch_year", "is_featured", "is_active", "order"]
    list_filter = ["is_featured", "is_active"]
    search_fields = ["name", "description"]
    list_editable = ["is_featured", "is_active", "order"]
    ordering = ["order", "-launch_year"]

    fieldsets = (
        ("Məhsul Məlumatları", {
            "fields": ("name", "tagline", "description", "launch_year")
        }),
        ("Linklər və Şəkil", {
            "fields": ("website_url", "instagram_url", "image")
        }),
        ("Göstəriş", {
            "fields": ("is_active", "is_featured", "order"),
            "classes": ("collapse",),
        }),
    )
