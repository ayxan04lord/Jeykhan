from django.shortcuts import render
from apps.core.models import TVShow, Product, ContactInfo


def projects(request):
    """Layihələr səhifəsi — verilişlər və məhsullar"""
    contact_info = ContactInfo.objects.filter(is_active=True).first()
    tv_shows = TVShow.objects.filter(is_active=True).order_by("order", "-year")
    products = Product.objects.filter(is_active=True).order_by("order", "-launch_year")

    context = {
        "contact_info": contact_info,
        "tv_shows": tv_shows,
        "products": products,
        "page_title": "Layihələr",
    }
    return render(request, "pages/projects/index.html", context)
