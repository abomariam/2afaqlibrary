from django.db import models
from stdimage.models import StdImageField
from stdimage.utils import UploadToUUID
# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=500)
    author = models.ForeignKey(Author, null=True, blank=True, related_name='books')
    category = models.ForeignKey(Category, null=True, blank=True, related_name='books')
    image = StdImageField(upload_to=UploadToUUID(path='books'), variations={
        'large': (1000, 500, True),
        'thumbnail': (200, 200, True),
        'medium': (483, 350, True),
    })
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(default=0.0)
    is_available = models.BooleanField(default=True)
    is_for_sale = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    @property
    def excerpt(self):
        words = self.description.split()
        if len(words) > 15:
            return ' '.join(words[:15]) + '...'
        return ' '.join(words)

    def __str__(self):
        return self.title