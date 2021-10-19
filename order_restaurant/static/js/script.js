$(document).ready(function () {
    var form = $('.form1');
    console.log(form);
    form.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number1').val();
        var submit_btn = $('#submit_btn1');
        var dish_id = submit_btn.data("dish_id");
        var dish_title = submit_btn.data("dish_title");
        var dish_price = submit_btn.data("dish_price");
        var total_dish_price = parseInt(dish_price) * parseInt(number);
        console.log(dish_id);
        console.log(dish_title);
        console.log(dish_price);

    var data = {};
    data.dish_id = dish_id;
    data.number = number;
    var csrf_token = $('.form1 [name="csrfmiddlewaretoken"]').val();
    data['csrfmiddlewaretoken'] = csrf_token;
    var url = "/basket_adding/";
    console.log(data.dish_id, data.number);

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            //console.log('OK');
            //console.log(data.dish_total_number);
            if (data.dish_total_number) {
                $('#basket_total_number').text("("+data.dish_total_number+")");

                console.log(data.dishes);
                $('.basket-items ol').html('');
                console.log('ok clear')
                $.each(data.dishes, function (k, v) {
                    $('.basket-items ol').append('<li>'+v.title+' '+v.item_number+'x'+v.price_per_item+' = '+total_dish_price+'грн. ' +
                        //'<a href="" class="delete-item">X</a>'// +
                        '</li>');
                console.log('ok append');
                })
            }

        },
        error: function (data) {
            console.log('error')
        },

    })


    });

    var form2 = $('.form2');
    console.log(form2);
    form2.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number2').val();
        console.log(number);
        var submit_btn = $('#submit_btn2');
        var dish_id = submit_btn.data("dish_id");
        var dish_title = submit_btn.data("dish_title");
        var dish_price = submit_btn.data("dish_price");
        var total_dish_price = parseInt(dish_price) * parseInt(number);
        console.log(dish_id);
        console.log(dish_title);
        console.log(dish_price);


    var data = {};
    data.dish_id = dish_id;
    data.number = number;
    var csrf_token = $('.form2 [name="csrfmiddlewaretoken"]').val();
    data['csrfmiddlewaretoken'] = csrf_token;
    var url = "/basket_adding/";
    console.log(data.dish_id, data.number);

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            //console.log('OK');
            //console.log(data.dish_total_number);
            if (data.dish_total_number) {
                $('#basket_total_number').text("("+data.dish_total_number+")");

                console.log(data.dishes);
                $('.basket-items ol').html('');
                console.log('ok clear')
                $.each(data.dishes, function (k, v) {
                    $('.basket-items ol').append('<li>'+v.title+' '+v.item_number+'x'+v.price_per_item+' = '+total_dish_price+'грн. ' +
                        //'<a href="" class="delete-item">X</a>'// +
                        '</li>');
                console.log('ok append');
                })
            }

        },
        error: function (data) {
            console.log('error')
        },

    })
    });

    var form3 = $('.form3');
    console.log(form3);
    form3.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number3').val();
        console.log(number);
        var submit_btn = $('#submit_btn3');
        var dish_id = submit_btn.data("dish_id");
        var dish_title = submit_btn.data("dish_title");
        var dish_price = submit_btn.data("dish_price");
        var total_dish_price = parseInt(dish_price) * parseInt(number);
        console.log(dish_id);
        console.log(dish_title);
        console.log(dish_price);


    var data = {};
    data.dish_id = dish_id;
    data.number = number;
    var csrf_token = $('.form3 [name="csrfmiddlewaretoken"]').val();
    data['csrfmiddlewaretoken'] = csrf_token;
    var url = "/basket_adding/";
    console.log(data.dish_id, data.number);

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            //console.log('OK');
            //console.log(data.dish_total_number);
            if (data.dish_total_number) {
                $('#basket_total_number').text("("+data.dish_total_number+")");

                console.log(data.dishes);
                $('.basket-items ol').html('');
                console.log('ok clear')
                $.each(data.dishes, function (k, v) {
                    $('.basket-items ol').append('<li>'+v.title+' '+v.item_number+'x'+v.price_per_item+' = '+total_dish_price+'грн. ' +
                        //'<a href="" class="delete-item">X</a>'// +
                        '</li>');
                console.log('ok append');
                })
            }

        },
        error: function (data) {
            console.log('error')
        },

    })
    });

    var form4 = $('.form4');
    console.log(form4);
    form4.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number4').val();
        console.log(number);
        var submit_btn = $('#submit_btn4');
        var dish_id = submit_btn.data("dish_id");
        var dish_title = submit_btn.data("dish_title");
        var dish_price = submit_btn.data("dish_price");
        var total_dish_price = parseInt(dish_price) * parseInt(number);
        console.log(dish_id);
        console.log(dish_title);
        console.log(dish_price);


            var data = {};
    data.dish_id = dish_id;
    data.number = number;
    var csrf_token = $('.form4 [name="csrfmiddlewaretoken"]').val();
    data['csrfmiddlewaretoken'] = csrf_token;
    var url = "/basket_adding/";
    console.log(data.dish_id, data.number);

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            //console.log('OK');
            //console.log(data.dish_total_number);
            if (data.dish_total_number) {
                $('#basket_total_number').text("("+data.dish_total_number+")");

                console.log(data.dishes);
                $('.basket-items ol').html('');
                console.log('ok clear')
                $.each(data.dishes, function (k, v) {
                    $('.basket-items ol').append('<li>'+v.title+' '+v.item_number+'x'+v.price_per_item+' = '+total_dish_price+'грн. ' +
                        //'<a href="" class="delete-item">X</a>'// +
                        '</li>');
                console.log('ok append');
                })
            }

        },
        error: function (data) {
            console.log('error')
        },

    })
    });

    var form5 = $('.form5');
    console.log(form5);
    form5.on('submit', function (e) {
        e.preventDefault();
        var number = $('#number5').val();
        console.log(number);
        var submit_btn = $('#submit_btn5');
        var dish_id = submit_btn.data("dish_id");
        var dish_title = submit_btn.data("dish_title");
        var dish_price = submit_btn.data("dish_price");
        var total_dish_price = parseInt(dish_price) * parseInt(number);
        console.log(dish_id);
        console.log(dish_title);
        console.log(dish_price);



    var data = {};
    data.dish_id = dish_id;
    data.number = number;
    var csrf_token = $('.form5 [name="csrfmiddlewaretoken"]').val();
    data['csrfmiddlewaretoken'] = csrf_token;
    var url = "/basket_adding/";
    console.log(data.dish_id, data.number);

    $.ajax({
        url: url,
        type: 'POST',
        data: data,
        cache: true,
        success: function (data) {
            //console.log('OK');
            //console.log(data.dish_total_number);
            if (data.dish_total_number) {
                $('#basket_total_number').text("("+data.dish_total_number+")");

                console.log(data.dishes);
                $('.basket-items ol').html('');
                console.log('ok clear')
                $.each(data.dishes, function (k, v) {
                    $('.basket-items ol').append('<li>'+v.title+' '+v.item_number+'x'+v.price_per_item+' = '+total_dish_price+'грн. ' +
                        //'<a href="" class="delete-item">X</a>'// +
                        '</li>');
                console.log('ok append');
                })
            }

        },
        error: function (data) {
            console.log('error')
        },

    })

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
        $(this).closest('li').remove();
    });


    function calculatingBasketPrice() {
        var total_order_price = 0;
        $('.total-dish-in-basket-price').each(function () {
            total_order_price += parseInt($(this).text());
        });
        $('#total_order_price').text(total_order_price);
    };

    $(document).on('click', ".plus-minus-button", function () {
        console.log('1')
        var current_number = $(this).siblings('.dish-in-basket-number').val();
        console.log(current_number);
        var current_tr = $(this).closest('tr');
        var current_price = parseInt(current_tr.find('.dish-price').text());
        var total_price = current_number*current_price;
        current_tr.find('.total-dish-in-basket-price').text(total_price + "грн.");
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
