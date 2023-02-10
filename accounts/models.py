from django.db import models
from location_field.models.plain import PlainLocationField

from phone_field import PhoneField
# Create your models here.

class Profile(models.Model):
    description = models.CharField(max_length=200),
    phone = PhoneField(blank=True, help_text='Contact phone number'),
    file = models.FileField(upload_to= 'files/', null=True)

    def __repr__(self):
        return 'Resume(%s, %s)' % (self.name, self.file)

class Place(models.Model):
    city = models.CharField(max_length=255),
    location = PlainLocationField(based_fields=['city'], zoom=7)

    def __str__(self):
        return self.location