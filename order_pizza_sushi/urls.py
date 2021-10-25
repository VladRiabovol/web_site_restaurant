from django.urls import path

from order_pizza_sushi import views

urlpatterns = [
    path('basket_adding_sushi_pizza/', views.basket_adding, name='basket_adding_sushi_pizza'),
    path('checkout_sushi_pizza/', views.checkout, name='checkout_sushi_pizza'),
    path('end_of_checkout_sushi_pizza/', views.end_of_checkout, name='end_of_checkout_sushi_pizza'),
]