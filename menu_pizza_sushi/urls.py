from django.urls import path
from menu_pizza_sushi import views

urlpatterns = [
    path('menu_sushi_pizza/', views.SushiPizzaDishesListView.as_view(), name='sushi-pizza-dishes-list'),
    path('menu_sushi_pizza/<slug:category>/', views.SushiPizzaCategoryListView.as_view(),
          name='sushi-pizza-category-list'),
]