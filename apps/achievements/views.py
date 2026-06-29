from django.shortcuts import render
from apps.core.models import Achievement, ContactInfo


def achievements(request):
    """Nailiyyətlər səhifəsi — sertifikat, medal, diplomlar"""
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    all_achievements = Achievement.objects.filter(is_active=True).order_by("order", "-year")

    # Group by type for section display
    gold_medals = all_achievements.filter(achievement_type="gold_medal")
    silver_medals = all_achievements.filter(achievement_type="silver_medal")
    bronze_medals = all_achievements.filter(achievement_type="bronze_medal")
    certificates = all_achievements.filter(achievement_type="certificate")
    diplomas = all_achievements.filter(achievement_type="diploma")
    awards = all_achievements.filter(achievement_type__in=["award", "title"])

    # Count stats
    total_medals = gold_medals.count() + silver_medals.count() + bronze_medals.count()

    context = {
        "contact_info": contact_info,
        "all_achievements": all_achievements,
        "gold_medals": gold_medals,
        "silver_medals": silver_medals,
        "bronze_medals": bronze_medals,
        "certificates": certificates,
        "diplomas": diplomas,
        "awards": awards,
        "total_medals": total_medals,
        "page_title": "Nailiyyətlər",
    }
    return render(request, "pages/achievements/index.html", context)
