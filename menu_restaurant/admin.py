from django.contrib import admin
from .models import Image, Category, Product
from .forms import CategoryForm, ProductForm
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


class ProductAdmin(admin.ModelAdmin):
    model = Product
    form = ProductForm
    fieldsets = (
        ('General', {
            'fields': ('title', 'description', 'category')
        }),
        ('Image', {
            'fields': ('image',)
        }),
        ('Price', {
            'fields': ('price', 'status')
        }),

    )
    list_display = (
        'title',
        'image',
        'slug',
    )
    search_fields = ('title', 'category', 'status')



admin.site.register(Image, ImageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
