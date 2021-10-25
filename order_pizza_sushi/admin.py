from django.contrib import admin
from order_pizza_sushi.models import Order, DishInOrder, DishInBasket

class DishInOrderInline(admin.TabularInline):
    model = DishInOrder
    extra = 0


class DishInOrderAdmin(admin.ModelAdmin):
    model = DishInOrder
    list_display = (
        'id', 'order', 'dish', 'total_price', 'created_at', 'updated_at'
    )

class DishInBasketAdmin(admin.ModelAdmin):
    model = DishInOrder
    list_display = (
        'id', 'session_key', 'order', 'dish', 'number', 'total_price',
        'is_active', 'created_at', 'updated_at'
    )

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [DishInOrderInline]
    list_display = (
        'id', 'created_at', 'name', 'phone', 'total_price', 'payment', 'change_from',
        'delivery', 'count_of_devices', 'street', 'house', 'entrance',
        'intercom', 'time_of_delivery', 'comments',
    )
    radio_fields = {
        'delivery': admin.HORIZONTAL,
        'payment': admin.HORIZONTAL,



    }
    list_filter = ()
    search_fields = ()

admin.site.register(Order, OrderAdmin)
admin.site.register(DishInOrder, DishInOrderAdmin)
admin.site.register(DishInBasket, DishInBasketAdmin)