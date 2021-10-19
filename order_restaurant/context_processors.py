from order_restaurant.models import DishInBasket


def getting_basket_info(request):
    session_key = request.session.session_key
    if not session_key:
        request.session['session_key'] = 123
        request.session.cycle_key()
    dishes_in_basket = DishInBasket.objects.filter(session_key=session_key, is_active=True)
    dish_total_number = dishes_in_basket.count()

    return locals()