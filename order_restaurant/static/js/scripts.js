$(document).ready(function () {

    function basketUpdating(dish_id, number, is_delete) {
        var data = {};
        data.dish_id = dish_id;
        //console.log('data.dish_id' + data.dish_id)
        data.number = number;
        //console.log('data.number' + data.number)
        var csrf_token = $('.form-dish [name="csrfmiddlewaretoken"]').val();
        if (csrf_token == undefined) {
            csrf_token = $('.form [name="csrfmiddlewaretoken"]').val();
        }
        data['csrfmiddlewaretoken'] = csrf_token;
        console.log(csrf_token);
        var url = "/basket_adding/";
        //console.log(data.dish_id, data.number);
        console.log(is_delete)
        if (is_delete == true ) {
            data["is_delete"] = true;
        };

        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            cache: true,
            success: function (data) {
                //console.log('OK');
                //console.log(data);
                //console.log(data.dish_total_number);
                if (data.dish_total_number) {
                    $('#basket_total_number').text("("+data.dish_total_number+")");

                    //console.log(data.dishes);
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

    $(document).on('submit', '.form-dish', function (e) {
        e.preventDefault();
        var number = $(this).find('.in-cart-input').val();
        //console.log(number + ' sibling');
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

    //$('.basket-container').on('click', function (e) {
    //    e.preventDefault();
    //    showingBasket();
    //});

    $('.basket-container').mouseover(function (e) {
        e.preventDefault();
        showingBasket();
    });

    $('.basket-container').mouseout(function (e) {
        e.preventDefault();
        showingBasket();
    });

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

        //console.log($(this).data);
        //dish_id = $(this).data('dish_id');
        //console.log(dish_id);
        //console.log('data from ondelete');

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

    $(document).on('click', ".plus-minus-button", function () {
        var current_number = $(this).siblings('.dish-in-basket-number').val();
        var current_tr = $(this).closest('tr');
        var current_price = parseInt(current_tr.find('.dish-price').text());
        var total_price = current_number*current_price;
        current_tr.find('.total-dish-in-basket-price').text(total_price + "₴");
        calculatingBasketPrice();
    });

    //$(document).on('change', "'.dish-in-basket-number'", function () {
    //    console.log('1')
    //    var current_number = $(this).val();
    //    console.log(current_number);
    //    var current_tr = $(this).closest('tr');
    //    var current_price = parseInt(current_tr.find('.dish-price').text());
    //    var total_price = current_number*current_price;
    //    current_tr.find('.total-dish-in-basket-price').text(total_price);
    //    calculatingBasketPrice();
    //});



    $(function(){
        $('input[type="number"]').niceNumber();
        });



    calculatingBasketPrice();
});
