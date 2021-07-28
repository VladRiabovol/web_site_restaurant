from django.db import models
import base64
from django.utils.text import slugify

class Image(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=False, upload_to='static/img/menu_pizza_sushi/')
    base_64 = models.CharField(blank=False, max_length=600000, default="", editable=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')

        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(max_length=300)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.0, max_digits=12, decimal_places=2)
    status = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.title