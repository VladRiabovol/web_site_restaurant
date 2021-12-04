from django.views.generic.list import ListView
from menu_pizza_sushi.models import Dish, Category


class SushiPizzaDishesListView(ListView):
    template_name = "menu_sushi_pizza.html"
    model = Dish

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.filter()
        context['dish_list'] = Dish.objects.all().order_by("category__slug")
        context['session_key'] = self.request.session.session_key if True else self.request.session.cycle_key()
        return context


class SushiPizzaCategoryListView(ListView):
    template_name = "menu_category_sushi_pizza.html"
    model = Dish

    def get_queryset(self):
        dishes = Dish.objects.filter(category__slug=self.kwargs['category'])
        return dishes

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['category'])
        context['categories_list'] = Category.objects.all().exclude(slug=context['category'].slug)
        context['session_key'] = self.request.session.session_key if True else self.request.session.cycle_key()
        return context

