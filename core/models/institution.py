from django.db import models
from django.core.validators import MinLengthValidator

class Institution(models.Model):
    name = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    address = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name 