from django.shortcuts import render
from apps.core.models import Restaurant, ContactInfo


def restaurants(request):
    """Restoranlar səhifəsi"""
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    restaurants_list = Restaurant.objects.filter(is_active=True).order_by("order", "name")

    context = {
        "contact_info": contact_info,
        "restaurants": restaurants_list,
        "page_title": "Restoranlar",
    }
    return render(request, "pages/restaurants/index.html", context)
