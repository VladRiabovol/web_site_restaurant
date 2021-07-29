from django import forms
from django import forms
from .models import Category, Dish

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

class DishForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ('title',
                  'description',
        )
        widgets = {
            'title': forms.TextInput,
            'description': forms.TextInput,
        }