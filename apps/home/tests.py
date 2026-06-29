from django.test import TestCase, Client
from django.urls import reverse
from apps.core.models import Service, Experience, ContactInfo


class HomeViewTest(TestCase):
    """Unit tests for home view"""

    def setUp(self):
        """Set up test data"""
        self.client = Client()
        self.contact = ContactInfo.objects.create(
            phone_number="+994501234567",
            email="test@example.com",
        )
        self.service = Service.objects.create(
            title="Test Service",
            category="restaurant",
            description="Test service description",
            icon="fas fa-test",
        )
        self.experience = Experience.objects.create(
            title="Test Experience",
            category="restaurant",
            description="Test experience description",
            years_experience=5,
            is_featured=True,
        )

    def test_home_view_status_code(self):
        """Test home view returns 200 status code"""
        response = self.client.get(reverse("home:home"))
        self.assertEqual(response.status_code, 200)

    def test_home_view_context(self):
        """Test home view context contains required data"""
        response = self.client.get(reverse("home:home"))
        self.assertIn("contact_info", response.context)
        self.assertIn("featured_services", response.context)
        self.assertIn("featured_experiences", response.context)
        self.assertEqual(response.context["contact_info"], self.contact)

    def test_home_view_template(self):
        """Test home view uses correct template"""
        response = self.client.get(reverse("home:home"))
        self.assertTemplateUsed(response, "pages/home/index.html")
