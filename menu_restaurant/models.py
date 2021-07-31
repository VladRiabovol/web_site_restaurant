from django.db import models
import base64
from django.utils.text import slugify

class Image(models.Model):
    title = models.CharField(max_length=50, verbose_name='Назва')
    image = models.ImageField(blank=False, upload_to='img/menu_restaurant/',
                              verbose_name='Зображення')
    base_64 = models.CharField(blank=False, max_length=600000, default="", editable=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')

        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Зображення'
        verbose_name_plural = 'Зображення'

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=300, verbose_name='Опис')
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Зображення')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Cтворенo')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Оновлено')


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

class Dish(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(max_length=300, verbose_name='Опис')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 verbose_name='Категорії')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='Зображення')
    price = models.DecimalField(default=0.0, max_digits=12, decimal_places=2,
                                verbose_name='Цiна')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Cтворенo')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Оновлено')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'