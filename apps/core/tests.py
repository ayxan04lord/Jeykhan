from django.test import TestCase
from django.core.exceptions import ValidationError
from hypothesis import given, strategies as st
from hypothesis.extra.django import TestCase as HypothesisTestCase
from .models import Service, Experience, ContactInfo


class ServiceModelTest(TestCase):
    """Unit tests for Service model"""

    def test_service_creation(self):
        """Test basic service creation"""
        service = Service.objects.create(
            title="Restaurant Consulting",
            category="restaurant",
            description="Professional restaurant management consulting services",
            icon="fas fa-utensils",
        )
        self.assertEqual(service.title, "Restaurant Consulting")
        self.assertEqual(service.category, "restaurant")
        self.assertTrue(service.is_active)
        self.assertEqual(service.order, 0)

    def test_service_string_representation(self):
        """Test service string representation"""
        service = Service.objects.create(
            title="Music Training",
            category="music",
            description="Professional vocal coaching and music training",
            icon="fas fa-music",
        )
        expected = "Music Training (Music Training)"
        self.assertEqual(str(service), expected)

    def test_service_ordering(self):
        """Test service ordering by order field and title"""
        service1 = Service.objects.create(
            title="B Service",
            category="restaurant",
            description="Second service description",
            icon="fas fa-utensils",
            order=2,
        )
        service2 = Service.objects.create(
            title="A Service",
            category="restaurant",
            description="First service description",
            icon="fas fa-utensils",
            order=1,
        )
        services = list(Service.objects.all())
        self.assertEqual(services[0], service2)  # Lower order first
        self.assertEqual(services[1], service1)


class ExperienceModelTest(TestCase):
    """Unit tests for Experience model"""

    def test_experience_creation(self):
        """Test basic experience creation"""
        experience = Experience.objects.create(
            title="Restaurant Management",
            category="restaurant",
            description="10 years managing high-end restaurants",
            years_experience=10,
        )
        self.assertEqual(experience.title, "Restaurant Management")
        self.assertEqual(experience.years_experience, 10)
        self.assertFalse(experience.is_featured)

    def test_experience_string_representation(self):
        """Test experience string representation"""
        experience = Experience.objects.create(
            title="Vocal Coaching",
            category="music",
            description="Professional vocal coaching experience",
            years_experience=5,
        )
        expected = "Vocal Coaching - 5 years (Music Training)"
        self.assertEqual(str(experience), expected)


class ContactInfoModelTest(TestCase):
    """Unit tests for ContactInfo model"""

    def test_contact_info_creation(self):
        """Test basic contact info creation"""
        contact = ContactInfo.objects.create(
            phone_number="+994501234567",
            email="test@example.com",
        )
        self.assertEqual(contact.phone_number, "+994501234567")
        self.assertEqual(contact.email, "test@example.com")
        self.assertTrue(contact.is_active)

    def test_contact_info_string_representation(self):
        """Test contact info string representation"""
        contact = ContactInfo.objects.create(
            phone_number="+994501234567",
            email="test@example.com",
        )
        expected = "Contact: +994501234567 (test@example.com)"
        self.assertEqual(str(contact), expected)

    def test_phone_number_validation(self):
        """Test phone number validation"""
        # Valid phone numbers
        valid_numbers = ["+994501234567", "994501234567", "+1234567890"]
        for number in valid_numbers:
            contact = ContactInfo(phone_number=number)
            contact.full_clean()  # Should not raise ValidationError

        # Invalid phone numbers
        invalid_numbers = ["123", "abc123", "+123456789012345678"]
        for number in invalid_numbers:
            contact = ContactInfo(phone_number=number)
            with self.assertRaises(ValidationError):
                contact.full_clean()


class PropertyBasedTests(HypothesisTestCase):
    """Property-based tests using Hypothesis"""

    @given(
        title=st.text(min_size=3, max_size=100),
        category=st.sampled_from(["restaurant", "music"]),
        description=st.text(min_size=10, max_size=1000),
        icon=st.text(min_size=1, max_size=50),
    )
    def test_property_6_content_management_integrity(
        self, title, category, description, icon
    ):
        """
        **Feature: jeykhan-portfolio, Property 6: Content Management Integrity**
        **Validates: Requirements 6.2, 6.4, 6.5**

        For any valid service data, the system should maintain data integrity
        during content updates and reflect changes immediately.
        """
        # Create service with generated data
        service = Service.objects.create(
            title=title,
            category=category,
            description=description,
            icon=icon,
        )

        # Verify data integrity
        self.assertEqual(service.title, title)
        self.assertEqual(service.category, category)
        self.assertEqual(service.description, description)
        self.assertEqual(service.icon, icon)
        self.assertTrue(service.is_active)  # Default value

        # Test immediate reflection of changes
        new_title = title + " Updated"
        service.title = new_title
        service.save()

        # Retrieve from database to verify persistence
        updated_service = Service.objects.get(id=service.id)
        self.assertEqual(updated_service.title, new_title)

    @given(
        phone=st.text(min_size=9, max_size=15).filter(lambda x: x.isdigit()),
    )
    def test_property_1_contact_button_functionality(self, phone):
        """
        **Feature: jeykhan-portfolio, Property 1: Contact Button Functionality**
        **Validates: Requirements 1.2, 1.3**

        For any valid phone number, the contact information should be properly
        formatted and accessible for tel: link functionality.
        """
        # Add country code prefix for valid format
        formatted_phone = f"+994{phone}"

        contact = ContactInfo.objects.create(
            phone_number=formatted_phone,
        )

        # Verify phone number is stored correctly
        self.assertEqual(contact.phone_number, formatted_phone)
        self.assertTrue(contact.is_active)

        # Verify contact can be retrieved for tel: link generation
        active_contact = ContactInfo.objects.filter(is_active=True).first()
        self.assertIsNotNone(active_contact)
        self.assertEqual(active_contact.phone_number, formatted_phone)

    @given(
        description=st.text(min_size=10, max_size=500),
    )
    def test_property_2_service_description_completeness(self, description):
        """
        **Feature: jeykhan-portfolio, Property 2: Service Description Completeness**
        **Validates: Requirements 2.4**

        For any service in the system, each service should have a non-empty
        description field that provides meaningful information.
        """
        service = Service.objects.create(
            title="Test Service",
            category="restaurant",
            description=description,
            icon="fas fa-test",
        )

        # Verify description is non-empty and meaningful
        self.assertIsNotNone(service.description)
        self.assertGreater(len(service.description.strip()), 0)
        self.assertGreaterEqual(
            len(service.description), 10
        )  # Minimum length validation
