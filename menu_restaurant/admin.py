from django.contrib import admin
from .models import Image, Category, Dish
from .forms import CategoryForm, DishForm
from admin_numeric_filter.admin import SliderNumericFilter

class ImageAdmin(admin.ModelAdmin):
    model = Image
    fieldsets = (
        ('General', {
             'fields': ('title', 'image',)
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
    form = CategoryForm
    fieldsets = (
        ('General', {
            'fields': ('title', 'description',)
        }),
        ('Image', {
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
    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'category')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Price', {
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