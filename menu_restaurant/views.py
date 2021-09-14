from django.views.generic.list import ListView
from menu_restaurant.models import Dish, Category, Image

# Create your views here.
class RestaurantDishesListView(ListView):
    template_name = "menu_dishes_restaurant.html"
    model = Dish

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.filter()
        context['dish_list'] = Dish.objects.all()
        return context



class RestaurantCategoryListView(ListView):
    template_name = "menu_category_restaurant.html"
    model = Dish

    def get_queryset(self):
        dishes = Dish.objects.filter(category__slug=self.kwargs['category'])
        return dishes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['categories_list'] = Category.objects.all().exclude(slug=context['category'].slug)
        return context
