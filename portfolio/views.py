from django.shortcuts import render
from .models import Service, Experience, ContactInfo


def home(request):
    """Ana səhifə görünüşü - Homepage view with featured content and contact info"""
    # Get active contact information
    contact_info = ContactInfo.objects.filter(is_active=True).first()

    # Get featured services (limit to 4 for homepage)
    featured_services = Service.objects.filter(is_active=True)[:4]

    # Get featured experiences for homepage highlights
    featured_experiences = Experience.objects.filter(is_featured=True)

    context = {
        "contact_info": contact_info,
        "featured_services": featured_services,
        "featured_experiences": featured_experiences,
        "page_title": "Ana Səhifə",
    }

    return render(request, "home.html", context)


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

    return render(request, "services.html", context)


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

    return render(request, "about.html", context)
