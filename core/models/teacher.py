from django.db import models
from django.core.validators import MinLengthValidator
from .institution import Institution

class Teacher(models.Model):
    """
    Model representing a teacher in the educational system.
    
    Attributes:
        first_name (CharField): Teacher's first name (minimum 2 characters)
        last_name (CharField): Teacher's last name (minimum 2 characters)
        email (EmailField): Teacher's email address
        phone (CharField): Teacher's phone number
        institution (ForeignKey): The institution where the teacher works
        hire_date (DateField): Date when the teacher was hired
        is_active (BooleanField): Whether the teacher is currently active
        created_at (DateTimeField): Timestamp of creation
        updated_at (DateTimeField): Timestamp of last update
    
    Properties:
        full_name: Returns the concatenation of first_name and last_name
    """
    first_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE, related_name='teachers')
    hire_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name 