from django.contrib import admin
from .models import ImagePizza, CategoryPizza, DishPizza
from django.utils.safestring import mark_safe
from admin_numeric_filter.admin import SliderNumericFilter

class ImageAdmin(admin.ModelAdmin):
    model = ImagePizza
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
    model = CategoryPizza
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
    model = DishPizza
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



admin.site.register(ImagePizza, ImageAdmin)
admin.site.register(CategoryPizza, CategoryAdmin)
admin.site.register(DishPizza, DishAdmin)
