from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date
from ..models import Institution, Teacher

class TeacherModelTest(TestCase):
    def setUp(self):
        self.institution = Institution.objects.create(
            name='Test School',
            address='123 Test Street',
            phone='+1234567890',
            email='test@school.com'
        )
        self.teacher_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@school.com',
            'phone': '+1234567890',
            'institution': self.institution,
            'hire_date': date.today()
        }

    def test_create_teacher(self):
        teacher = Teacher.objects.create(**self.teacher_data)
        self.assertEqual(teacher.full_name, 'John Doe')
        self.assertEqual(teacher.institution, self.institution)

    def test_teacher_name_validation(self):
        # Test minimum length validation
        self.teacher_data['first_name'] = 'A'
        teacher = Teacher(**self.teacher_data)
        with self.assertRaises(ValidationError):
            teacher.full_clean()

    def test_teacher_str_representation(self):
        teacher = Teacher.objects.create(**self.teacher_data)
        self.assertEqual(str(teacher), 'John Doe')

    def test_teacher_full_name_property(self):
        teacher = Teacher.objects.create(**self.teacher_data)
        self.assertEqual(teacher.full_name, 'John Doe') 