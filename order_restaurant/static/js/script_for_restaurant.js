$(document).ready(function () {

    function basketUpdating(dish_id, number, is_delete) {
        var data = {};
        data.dish_id = dish_id;
        data.number = number;
        var csrf_token = $('.form-dish [name="csrfmiddlewaretoken"]').val();
        if (csrf_token == undefined) {
            csrf_token = $('.form [name="csrfmiddlewaretoken"]').val();
        }
        data['csrfmiddlewaretoken'] = csrf_token;
        var url = "/basket_adding/";
        if (is_delete == true ) {
            data["is_delete"] = true;
        };

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                if (data.dish_total_number) {
                    $('.count-basket').text(data.dish_total_number);
                    $('.basket-items ol').html('');
                    $.each(data.dishes, function (k, v) {
                        $('.basket-items ol').append('<li>'+v.title+' '+v.item_number+' шт по '+v.price_per_item+ '</li>');
                    })
                }

            },
            error: function (data) {
                console.log('error')
            },

    });
    };

    //add dish to basket.
    $(document).on('submit', '.form-dish', function (e) {
        e.preventDefault();
        var number = $(this).find('.in-cart-input').val();
        var submit_btn = $(this).find('.in-cart-button');
        var dish_id = submit_btn.data("dish_id");
        var dish_title = submit_btn.data("dish_title");
        var dish_price = submit_btn.data("dish_price");
        console.log(dish_id);
        console.log(dish_title);
        console.log(dish_price);

        basketUpdating(dish_id, number, is_delete=false)
    });

    function showingBasket() {
        $('.basket-items').toggleClass('hidden');
    };
    $('.basket-container').mouseover(function (e) {
        e.preventDefault();
        showingBasket();
    });
    $('.basket-container').mouseout(function (e) {
        e.preventDefault();
        showingBasket();
    });

    //delete dish from basket.
    $(document).on('click', '.delete-item', function (e) {
        e.preventDefault();
        var dish_id = $(this).data("dish_id");
        var dish_title = $(this).data("dish_title");
        var dish_price = $(this).data("dish_price");
        var number = $('.dish-in-basket-number').val();
        console.log(dish_id);
        console.log(dish_title);
        console.log(dish_price);
        console.log('number ' + number);

        basketUpdating(dish_id, number, is_delete=true)
        $(this).closest('tr').remove();
    });

    function calculatingBasketPrice() {
        var total_order_price = 0;
        $('.total-dish-in-basket-price').each(function () {
            total_order_price += parseInt($(this).text());
        });
        $('#total_order_price').text(total_order_price);
    };

    //change quantity of dishes in basket.
    $(document).on('click', ".plus-minus-button", function () {
        var current_number = $(this).siblings('.dish-in-basket-number').val();
        var current_tr = $(this).closest('tr');
        var current_price = parseInt(current_tr.find('.dish-price').text());
        var total_price = current_number*current_price;
        current_tr.find('.total-dish-in-basket-price').text(total_price + "₴");
        calculatingBasketPrice();
    });

    $(function(){
        $('input[type="number"]').niceNumber();
        });

    calculatingBasketPrice();
});
