from django.http import JsonResponse
from order_pizza_sushi.models import DishInBasket, DishInOrder, Order
from django.shortcuts import render
from order_pizza_sushi.forms import OrderForm
from django.shortcuts import redirect
from django.urls import reverse
from bot import bot


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    if not session_key:
        request.session['session_key'] = 123
        request.session.cycle_key()
    data = request.POST
    dish_id = data.get('dish_id')
    number = data.get('number')
    is_delete = data.get('is_delete')

    if is_delete == 'true':
        print(f'delete {data}')
        DishInBasket.objects.filter(id=dish_id).delete()
    else:
        new_dish, created = DishInBasket.objects.get_or_create(session_key=session_key,
                                                                  dish_id=dish_id,
                                                                  defaults={'number': number})

        print(f'not delete {new_dish, created}')
        if not created:
            new_dish.number += int(number)
            new_dish.save(force_update=True)

    # code for 2 cases
    dishes_in_basket_sp = DishInBasket.objects.filter(session_key=session_key, is_active=True)
    dish_total_number_sp = dishes_in_basket_sp.count()
    return_dict['dish_total_number'] = dish_total_number_sp
    return_dict['dishes'] = list()
    for item in dishes_in_basket_sp:
        dish_dict = dict()
        dish_dict['title'] = item.dish.title
        dish_dict['price_per_item'] = item.price_per_item
        dish_dict['item_number'] = item.number
        return_dict['dishes'].append(dish_dict)
    return JsonResponse(return_dict)

def checkout(request):
    session_key = request.session.session_key
    dishes_in_basket = DishInBasket.objects.filter(session_key=session_key, is_active=True).exclude(order__isnull=False)
    form = OrderForm(request.POST or None)
    if request.POST:
        if form.is_valid():
            data = request.POST
            name = data.get('name', 'Уточнить')
            phone = data.get('phone')
            payment = data.get('payment')
            delivery = data.get('delivery')
            change_from = data.get('change_from', 'Уточнить')
            count_of_devices = data.get('count_of_devices', 'Уточнить')
            street = data.get('street', 'Уточнить')
            house = data.get('house', 'Уточнить')
            entrance = data.get('entrance', 'Уточнить')
            intercom = data.get('intercom', 'Уточнить')
            time_of_delivery = data.get('time_of_delivery', 'Уточнить')
            comments = data.get('comments', 'Уточнить')


            order = Order.objects.create(name=name, phone=phone, payment=payment, delivery=delivery,
                                         change_from=change_from, count_of_devices=count_of_devices,
                                         street=street, house=house, entrance=entrance, intercom=intercom,
                                         time_of_delivery=time_of_delivery, comments=comments)
            dishes_in_order_bot = ""
            total_price_bot = 0
            for name, value in data.items():

                if name.startswith('dish_in_basket_'):
                    dish_in_basket_id = name.split('dish_in_basket_')[1]
                    dish_in_basket = DishInBasket.objects.get(id=dish_in_basket_id)


                    dish_in_basket.number = value
                    dish_to_bot = str(dish_in_basket.dish.title) + ': ' + str(value) + 'шт\n'
                    dishes_in_order_bot += dish_to_bot
                    total_price_bot += int(dish_in_basket.dish.price) * int(value)
                    print(dishes_in_order_bot)

                    dish_in_basket.save(force_update=True)

                    DishInOrder.objects.create(dish=dish_in_basket.dish, number=dish_in_basket.number,
                                               price_per_item=dish_in_basket.price_per_item,
                                               total_price=dish_in_basket.price_per_item,
                                               order=order)

            message = f'Пришел заказ: Суши-пицца \nИмя: {name} \nТелефон: {phone} \n' \
                      f'Доставка: {delivery} \n' \
                      f'Время доставки: {time_of_delivery} \nОплата: {payment} \nСдача с: {change_from} \n' \
                      f'Приборы: {count_of_devices} \nУлица: {street} \nДом: {house} \n' \
                      f'Подьезд: {entrance} \nДомофон: {intercom} \nКоментарий: {comments}\n' \
                      f'Блюда: \n{dishes_in_order_bot}' \
                      f'Сумма заказа: {total_price_bot}'


            bot.bot.send_message(bot.CHAT_ID, message)
            request.session.cycle_key()

            return redirect(reverse('end_of_checkout'))
        else:
            return render(request, 'checkout_sushi_pizza.html', locals())
    return render(request, 'checkout_sushi_pizza.html', locals())

def end_of_checkout(request):
    return render(request, 'end_of_checkout.html')
