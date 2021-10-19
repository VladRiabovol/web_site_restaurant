from django import forms
from django.core.validators import RegexValidator
from django.forms import ModelForm
from order_restaurant.models import Order
from datetime import time

class OrderForm(forms.Form):
    DELIVERY = (
        ('Доставка', 'Доставка'),
        ('Заберу сам(а)', 'Заберу сам(а)'),
    )
    PAYMENT = (
        ('Наличные', 'Наличные'),
        ('Карта', 'Карта'),
    )
    CHOICES_FOR_TIME = tuple((time(hour=hour, minute=minute), f'{hour}:{minute}')
                             for hour in range(11, 22)
                             for minute in range(0, 59, 15))


    widget_attrs = {'class': 'form-control'}
    phone_regex = RegexValidator(regex=r'^\+?1?\d{12,15}$',
                                 message="Телефон должен быть в формате '+380.........'")

    name = forms.CharField(label='Имя', widget=forms.widgets.TextInput(
                                        attrs={**widget_attrs, **{'id': 'fieldName'}}))
    phone = forms.CharField(label="Телефон",
                            validators=[phone_regex], max_length=17,
                            widget=forms.widgets.TextInput(
                                attrs={**widget_attrs, **{'id': 'fieldPhone'}}))
    payment = forms.ChoiceField(label='Оплата',
                              choices=PAYMENT,
                              widget=forms.RadioSelect(attrs={ **{'id': 'fieldPhone'}}))
    delivery = forms.ChoiceField(label='Доставка',
                                 choices=DELIVERY,
                                 widget=forms.widgets.RadioSelect(attrs={**{'id': 'fieldDelivery'}}))
    change_from = forms.CharField(label='Сдача с', required=False,
                                  widget=forms.widgets.TextInput(
                                  attrs={**widget_attrs, **{'id': 'fieldChange_From',}}))
    count_of_devices = forms.CharField(label='Колличество приборов', required=False,
                                       widget=forms.widgets.TextInput(
                                       attrs={**widget_attrs, **{'id': 'fieldCount_Of_Devices'}}))
    street = forms.CharField(label='Улица',
                             widget=forms.widgets.TextInput(
                             attrs={**widget_attrs, **{'id': 'fieldStreet'}}))
    house = forms.CharField(label='Дом',
                            widget=forms.widgets.TextInput(
                            attrs={**widget_attrs, **{'id': 'fieldHouse'}}))
    entrance = forms.CharField(label='Подъезд', required=False,
                               widget=forms.widgets.TextInput(
                               attrs={**widget_attrs, **{'id': 'fieldEntrance'}}))
    intercom = forms.CharField(label='Домофон', required=False,
                               widget=forms.widgets.TextInput(
                               attrs={**widget_attrs, **{'id': 'fieldIntercom'}}))
    time_of_delivery = forms.ChoiceField(label='Время доставки', required=False,
                                         choices=CHOICES_FOR_TIME,
                                         widget=forms.widgets.Select())
    comments = forms.CharField(label='Комментарий', required=False,
                               widget=forms.widgets.TextInput(
                               attrs={**widget_attrs, **{'id': 'fieldComments'}}))