from django.db import models
from django.core.validators import validate_image_file_extension
from django.urls import reverse

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=255, blank=True)
    cart_image = models.ImageField(upload_to='photos/categories', blank=True, validators=[validate_image_file_extension])

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
            return reverse('products_by_category',args=[self.slug])

    def __str__(self):
        return self.category_name

