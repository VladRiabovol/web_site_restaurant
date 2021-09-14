from django.contrib import admin
from menu_restaurant.models import Image, Category, Dish
from django.utils.safestring import mark_safe


class ImageAdmin(admin.ModelAdmin):
    model = Image
    prepopulated_fields = { 'slug' : ('title',), }
    fieldsets = (
        ('Загальнi', {
             'fields': ('title', 'image', 'slug',)
        }),
    )
    list_display = (
        'title',
        'get_image',
    )
    search_fields = ('title',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url}" width="100" height="60">')

    get_image.short_description = 'Зображення'



class CategoryAdmin(admin.ModelAdmin):
    model = Category
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = (
        ('Загальнi', {
            'fields': ('title', 'description', 'slug',)
        }),
        ('Зображення', {
            'fields': ('image',)
        }),

    )
    list_display = (
        'title',
        'slug',
        'description',
        'image',

    )
    search_fields = ('title',)


class DishAdmin(admin.ModelAdmin):
    model = Dish
    prepopulated_fields = {'slug': ('title',), }
    fieldsets = (
        ('Загальнi', {
            'fields': ('title', 'description', 'category', 'slug',)
        }),
        ('Зображення', {
            'fields': ('image',)
        }),
        ('Цiна', {
            'fields': ('price',)
        }),

    )
    list_display = (
        'title',
        'get_image',
        'description',
        'category',
        'price',

    )
    search_fields = ('title', 'category',)

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.image.url}" width="100" height="60">')

    get_image.short_description = 'Зображення'



admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)
