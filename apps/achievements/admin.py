from django.contrib import admin
from unfold.admin import ModelAdmin
from apps.core.models import Achievement


@admin.register(Achievement)
class AchievementAdmin(ModelAdmin):
    list_display = ["title", "achievement_type", "issuer", "year", "competition_name", "is_active", "order"]
    list_filter = ["achievement_type", "year", "is_active"]
    search_fields = ["title", "issuer", "competition_name", "description"]
    list_editable = ["is_active", "order"]
    ordering = ["order", "-year"]

    fieldsets = (
        ("Nailiyyət Məlumatları", {
            "fields": ("title", "achievement_type", "issuer", "year", "competition_name")
        }),
        ("Ətraflı", {
            "fields": ("description", "image")
        }),
        ("Göstəriş", {
            "fields": ("is_active", "order"),
            "classes": ("collapse",),
        }),
    )
