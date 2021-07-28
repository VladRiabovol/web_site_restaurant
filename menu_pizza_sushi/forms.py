from django import forms
from .models import Category, Product

class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = (
                  'title',
                  'description',
        )
        widgets = {
            'title': forms.TextInput,
            'description': forms.TextInput,
        }

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('title',
                  'description',
        )
        widgets = {
            'title': forms.TextInput,
            'description': forms.TextInput,
        }