from django.db import models
from django.core.validators import MinLengthValidator

class Institution(models.Model):
    """
    Model representing an educational institution.
    
    Attributes:
        name (CharField): The name of the institution (minimum 3 characters)
        address (TextField): The physical address of the institution
        phone (CharField): Contact phone number
        email (EmailField): Contact email address
        website (URLField): Institution's website (optional)
        created_at (DateTimeField): Timestamp of creation
        updated_at (DateTimeField): Timestamp of last update
    """
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 