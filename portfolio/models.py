from django.db import models

# Create your models here.

class Image(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='image/', null=True, max_length=255)

    def __repr__(self):
        return 'Image(%s, %s)' % (self.tile, self.image)

    def __str__(self):
        return self.title
