from django.shortcuts import render
from apps.core.models import Service, ContactInfo


def services(request):
    """Xidmətlər səhifəsi görünüşü - Services page with categorized services"""
    # Get active contact information
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    # Get services by category
    restaurant_services = Service.objects.filter(
        category="restaurant", is_active=True
    ).order_by("order", "title")

    music_services = Service.objects.filter(category="music", is_active=True).order_by(
        "order", "title"
    )

    context = {
        "contact_info": contact_info,
        "restaurant_services": restaurant_services,
        "music_services": music_services,
        "page_title": "Xidmətlər",
    }

    return render(request, "pages/services/index.html", context)
