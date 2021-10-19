from django.db import models
import base64
from django.utils.text import slugify

class Image(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(blank=False, upload_to='img/menu_restaurant/',
                              verbose_name='Изображение')
    base_64 = models.CharField(blank=False, max_length=600000, default="", editable=False)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.base_64 = base64.b64encode(self.image.read()).decode('utf-8')

        super(Image, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображение'

class Category(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    description = models.TextField(max_length=300, verbose_name='Описание', blank=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, blank=True,
                              verbose_name='Изображение')
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,
                                      verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True,
                                      verbose_name='Обновлено')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Dish(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    description = models.TextField(max_length=300, verbose_name='Описание')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,
                                 verbose_name='Категории')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, verbose_name='Изображение')
    price = models.DecimalField(default=0.0, max_digits=12, decimal_places=0,
                                verbose_name='Цена')
    is_active = models.BooleanField(default=True)
    slug = models.SlugField(unique=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')

    def __str__(self):
        return f'{self.title} {self.price}грн.'

    @property
    def get_description(self):
        return [self.description]


    class Meta:
        verbose_name = 'Блюдо'
        verbose_name_plural = 'Блюда'
