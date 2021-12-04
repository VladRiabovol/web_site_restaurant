from datetime import time
from django.db import models
from django.db.models.signals import post_save
from menu_restaurant.models import Dish


class Order(models.Model):
    DELIVERY = (
        ('Доставка', 'Доставка'),
        ('Заберу сам(а)', 'Заберу сам(а)'),
    )
    PAYMENT = (
        ('Наличные','Наличные'),
        ('Карта', 'Карта'),
    )
    CHOICES_FOR_TIME = tuple((time(hour=hour, minute=minute), f'{hour}:{minute}')
                             for hour in range(11, 22)
                             for minute in range(0, 59, 15))

    name = models.CharField(max_length=100, verbose_name="Ваше имя")
    phone = models.CharField(max_length=17, verbose_name='Телефон')
    payment = models.CharField(max_length=50, choices=PAYMENT, verbose_name='Оплата')
    change_from = models.CharField(blank=True, max_length=50, verbose_name='Сдача с')
    delivery = models.CharField(max_length=50, choices=DELIVERY, verbose_name='Доставка')
    count_of_devices = models.CharField(blank=True, verbose_name='Колличество приборов', max_length=2 )
    street = models.CharField(blank=True, max_length=50, default='Уточнить', verbose_name='Улица')
    house = models.CharField(blank=True, max_length=10, default='Уточнить', verbose_name='Дом')
    entrance = models.CharField(blank=True, max_length=10, default='Уточнить', verbose_name="Подъезд")
    intercom = models.CharField(blank=True, max_length=10, default='Уточнить', verbose_name="Домофон")
    time_of_delivery = models.TimeField(choices=CHOICES_FOR_TIME, blank=True, default='Как можно раньше',
                                        verbose_name='Время доставки')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name='Цена заказа')
    comments = models.CharField(blank=True, max_length=500, verbose_name='Коментарий')
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return f'Заказ {self.id}'

    def save(self, *args, **kwargs):

        super(Order, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class DishInOrder(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
                              blank=True, null=True, default=None)
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL,
                             blank=True, null=True, default=None)
    number = models.IntegerField(default=0, verbose_name='Колличество')
    price_per_item = models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name='Цена за ед.')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Всего') #price*number
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return f'{self.dish.title}'


    class Meta:
        verbose_name = 'Блюда в заказе'
        verbose_name_plural = 'Блюда в заказе'

    def save(self, *args, **kwargs):
        price_per_item = self.dish.price
        self.price_per_item = price_per_item
        self.total_price = int(self.number) * price_per_item
        super(DishInOrder, self).save(*args, **kwargs)

def dishes_in_order_post_save(sender, instance, created, **kwargs):
        order = instance.order
        all_dishes_in_order = DishInOrder.objects.filter(order=order)
        order_total_price = 0
        for item in all_dishes_in_order:
            order_total_price += item.total_price
        instance.order.total_price = order_total_price
        instance.order.save(force_update=True)

post_save.connect(dishes_in_order_post_save, sender=DishInOrder)

class DishInBasket(models.Model):
    session_key = models.CharField(max_length=128, default=None)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL,
                              blank=True, null=True, default=None)
    dish = models.ForeignKey(Dish, on_delete=models.SET_NULL,
                             blank=True, null=True, default=None)
    number = models.IntegerField(default=0, verbose_name='Колличество')
    is_active = models.BooleanField(default=True)
    price_per_item = models.DecimalField(max_digits=5, decimal_places=0, default=0, verbose_name='Цена за ед.')
    total_price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name='Всего') #price*number
    created_at = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Создано')
    updated_at = models.DateTimeField(auto_now=True, null=True, verbose_name='Обновлено')

    def __str__(self):
        return f'{self.dish.title}'


    class Meta:
        verbose_name = 'Блюда в корзине'
        verbose_name_plural = 'Блюда в корзине'

    def save(self, *args, **kwargs):
        price_per_item = self.dish.price
        self.price_per_item = price_per_item
        self.total_price = int(self.number) * price_per_item
        super(DishInBasket, self).save(*args, **kwargs)
