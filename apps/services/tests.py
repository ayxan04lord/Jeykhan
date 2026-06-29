from django.test import TestCase, Client
from django.urls import reverse
from apps.core.models import Service, ContactInfo


class ServicesViewTest(TestCase):
    """Unit tests for services view"""

    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.contact = ContactInfo.objects.create(
            phone_number="+994501234567",
            email="test@example.com",
        )
        self.restaurant_service = Service.objects.create(
            title="Restaurant Service",
            category="restaurant",
            description="Restaurant service description",
            icon="fas fa-utensils",
        )
        self.music_service = Service.objects.create(
            title="Music Service",
            category="music",
            description="Music service description",
            icon="fas fa-music",
        )

    def test_services_view_status_code(self):
        """Test services view returns 200 status code"""
        response = self.client.get(reverse("services:services"))
        self.assertEqual(response.status_code, 200)

    def test_services_view_context(self):
        """Test services view context contains categorized services"""
        response = self.client.get(reverse("services:services"))
        self.assertIn("contact_info", response.context)
        self.assertIn("restaurant_services", response.context)
        self.assertIn("music_services", response.context)

        # Check that services are properly categorized
        restaurant_services = list(response.context["restaurant_services"])
        music_services = list(response.context["music_services"])

        self.assertIn(self.restaurant_service, restaurant_services)
        self.assertIn(self.music_service, music_services)

    def test_services_view_template(self):
        """Test services view uses correct template"""
        response = self.client.get(reverse("services:services"))
        self.assertTemplateUsed(response, "pages/services/index.html")
