from django.contrib import admin
from .models import Order, Cart
from admin_numeric_filter.admin import SliderNumericFilter

class CartAdmin(admin.ModelAdmin):
    model = Cart
    list_display = (
        'created_at', 'quantity', 'total_price', 'updated_at',
    )

class OrderAdmin(admin.ModelAdmin):
    model = Order
    actions_on_top = True
    fieldsets = (
        ('Загальнi', {
            'fields': ('name', 'phone', 'cart')
        }),
        ('Оплата', {
            'fields': ('payment', 'change_from')
        }),
        ('Доставка', {
            'fields': ('delivery', 'count_of_devices', 'street',
                       'house', 'entrance', 'intercom', 'do_not_call',
                       'time_of_delivery',)
        }),
        ('Коментар до заказу', {
            'classes': ('collapse',),
            'fields': ('comments',)
        }),

    )
    list_display = (
        'created_at', 'name', 'phone', 'cart', 'payment', 'change_from',
        'delivery', 'count_of_devices', 'street', 'house', 'entrance',
        'intercom', 'do_not_call', 'time_of_delivery', 'comments',
    )
    radio_fields = {
        'delivery': admin.HORIZONTAL,
        'payment': admin.HORIZONTAL,



    }
    list_filter = ('created_at', 'delivery', 'payment')
    search_fields = ('created_at', 'name', 'payment')

admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)