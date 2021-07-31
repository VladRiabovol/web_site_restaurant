from django.db import models
from menu_pizza_sushi.models import Dish
from datetime import time


class Cart(models.Model):
    total_price = models.FloatField(blank=True, null=True,
                                    verbose_name='Разом')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Кiлькiсть')
    created_at = models.DateTimeField(auto_now_add=True, null=True,
                                      verbose_name='Cтворенo')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')

    class Meta:
        verbose_name = 'Кошик'
        verbose_name_plural = 'Кошик'

class Order(models.Model):
    DELIVERY = (
        ('Доставка', 'Доставка'),
        ('Забрати з ресторану', 'Забрати з ресторану'),
    )
    PAYMENT = (
        ('Готівка','Готівка'),
        ('Картка', 'Картка'),
    )
    CHOICES_FOR_TIME = tuple((time(hour=hour, minute=minute), f'{hour}:{minute}')
                             for hour in range(11, 22)
                             for minute in range(0, 59, 15))

    cart = models.OneToOneField(Cart, on_delete=models.CASCADE,
                                null=True, verbose_name='Кошик')
    name = models.CharField(max_length=100, verbose_name="Ваше ім'я")
    phone = models.CharField(max_length=17, verbose_name='Телефон')
    payment = models.CharField(max_length=50, choices=PAYMENT, verbose_name='Оплата')
    change_from = models.CharField(blank=True, max_length=50, verbose_name='Решта з')
    delivery = models.CharField(max_length=50, choices=DELIVERY, verbose_name='Доставка')
    count_of_devices = models.PositiveIntegerField(blank=True, verbose_name='Кількість приборів')
    street = models.CharField(blank=True, max_length=50, default='Уточнити', verbose_name='Вулиця')
    house = models.CharField(blank=True, max_length=10, default='Уточнити', verbose_name='Будинок')
    entrance = models.CharField(blank=True, max_length=10, default='Уточнити', verbose_name="Під'їзд")
    intercom = models.CharField(blank=True, max_length=10, default='Уточнити', verbose_name="Домофон")
    do_not_call = models.BooleanField(blank=True, verbose_name='Не дзвонити мені')
    time_of_delivery = models.TimeField(choices=CHOICES_FOR_TIME, blank=True, default='Як можна ранiше',
                                        verbose_name='Час доставки')
    comments = models.CharField(blank=True, max_length=500, verbose_name='Коментар')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Cтворенo')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Оновлено')

    def __str__(self):
        return f'{self.name}, {self.delivery}, {self.payment}, сумма: {self.cart.total_price}'

    class Meta:
        verbose_name = 'Замовлення'
        verbose_name_plural = 'Замовлення'
