from django.core.validators import FileExtensionValidator
from .validators import name_file
from django.db import models


# Create your models here.
class Documents(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=100)
    upload_file = models.FileField(upload_to=name_file, blank=False, validators=[FileExtensionValidator(['pdf', 'zip'])], )
