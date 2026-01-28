from django.shortcuts import render
from apps.core.models import Experience, ContactInfo


def about(request):
    """Haqqında səhifəsi görünüşü - About page with professional background"""
    # Get active contact information
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    # Get all experiences organized by category
    restaurant_experiences = Experience.objects.filter(category="restaurant").order_by(
        "order", "-years_experience"
    )

    music_experiences = Experience.objects.filter(category="music").order_by(
        "order", "-years_experience"
    )

    # Get all experiences for general display
    all_experiences = Experience.objects.all().order_by("order", "-years_experience")

    context = {
        "contact_info": contact_info,
        "restaurant_experiences": restaurant_experiences,
        "music_experiences": music_experiences,
        "all_experiences": all_experiences,
        "page_title": "Haqqında",
    }

    return render(request, "pages/about/index.html", context)
