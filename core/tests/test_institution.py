from django.test import TestCase
from django.core.exceptions import ValidationError
from ..models import Institution

class InstitutionModelTest(TestCase):
    def setUp(self):
        self.institution_data = {
            'name': 'Test School',
            'address': '123 Test Street',
            'phone': '+1234567890',
            'email': 'test@school.com',
            'website': 'https://testschool.com'
        }

    def test_create_institution(self):
        institution = Institution.objects.create(**self.institution_data)
        self.assertEqual(institution.name, 'Test School')
        self.assertEqual(institution.email, 'test@school.com')

    def test_institution_name_validation(self):
        # Test minimum length validation
        self.institution_data['name'] = 'AB'
        institution = Institution(**self.institution_data)
        with self.assertRaises(ValidationError):
            institution.full_clean()

    def test_institution_str_representation(self):
        institution = Institution.objects.create(**self.institution_data)
        self.assertEqual(str(institution), 'Test School') 