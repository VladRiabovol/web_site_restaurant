from django.contrib import admin
from .models import Image, Category, Dish
from .forms import CategoryForm, DishForm
from admin_numeric_filter.admin import SliderNumericFilter

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
        'image',
        'slug',
    )
    search_fields = ('title',)

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
    form = DishForm
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
        'image',
        'slug',
    )
    search_fields = ('title', 'category',)



admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Dish, DishAdmin)