from django.urls import path
from menu_restaurant import views

urlpatterns = [
    path('menu_restaurant/', views.RestaurantDishesListView.as_view(), name='restaurant-dishes-list'),
    path('menu_restaurant/<slug:category>/', views.RestaurantCategoryListView.as_view(),
          name='restaurant-category-list'),
]