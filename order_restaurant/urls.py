from django.urls import path
from order_restaurant import views

urlpatterns = [
    path('basket_adding/', views.basket_adding, name='basket_adding'),
    path('checkout/', views.checkout, name='checkout'),
    path('end_of_checkout/', views.end_of_checkout, name='end_of_checkout'),
    path('back_call/', views.back_call, name='back_call'),
    path('end_of_back_call/', views.end_of_back_call, name='end_of_back_call'),
    path('about_us/', views.about_us, name='about_us'),
]