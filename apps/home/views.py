from django.shortcuts import render
from apps.core.models import Service, Experience, ContactInfo


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

    return render(request, "pages/home/index.html", context)
