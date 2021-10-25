from order_pizza_sushi.models import DishInBasket


def getting_basket_info_sp(request):
    session_key = request.session.session_key
    if not session_key:
        request.session['session_key'] = 123
        request.session.cycle_key()
    dishes_in_basket_sp = DishInBasket.objects.filter(session_key=session_key, is_active=True)
    dish_total_number_sp = dishes_in_basket_sp.count()

    return locals()