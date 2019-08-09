document.addEventListener("DOMContentLoaded", () => {

    // order page dropdown menu functionality
    $("#id_meal").change(function () {
        var mealId = $(this).val();
        if (mealId != "") {
            var url_meal_type = $("#orderForm").attr("data-meal_type-url");
            var url_size = $("#orderForm").attr("data-size-url");
            var url_meal_addition = $("#orderForm").attr("data-meal_addition-url");
            // once a meal is seleceted then send ajax request for the meal types data
            $.ajax({
                url: url_meal_type,
                data: {
                    'meal': mealId
                },
                success: function (data) {
                    $("#id_meal_type").html(data);
                }
            });
            $.ajax({
                url: url_size,
                data: {
                    'meal_type': 0
                },
                success: function (data) {
                    $("#id_size").html(data);
                }
            });
            $.ajax({
                url: url_meal_addition,
                data: {
                    'meal_type': 0
                },
                success: function (data) {
                    $("#id_meal_addition").html(data);
                }
            });
        }
        else {
            var url_meal_type = $("#orderForm").attr("data-meal_type-url");
            var url_size = $("#orderForm").attr("data-size-url");
            var url_meal_addition = $("#orderForm").attr("data-meal_addition-url");
            $.ajax({
                url: url_meal_type,
                data: {
                    'meal': 0
                },
                success: function (data) {
                    $("#id_meal_type").html(data);
                }
            });
            $.ajax({
                url: url_size,
                data: {
                    'meal_type': 0
                },
                success: function (data) {
                    $("#id_size").html(data);
                }
            });
            $.ajax({
                url: url_meal_addition,
                data: {
                    'meal_type': 0
                },
                success: function (data) {
                    $("#id_meal_addition").html(data);
                }
            });
        };
    });
    $("#id_meal_type").change(function () {
        var url_size = $("#orderForm").attr("data-size-url");
        var url_meal_addition = $("#orderForm").attr("data-meal_addition-url");
        var meal_typeId = $(this).val();
        // once a meal type is seleceted then send ajax requests for both the size and additions data
        $.ajax({
            url: url_size,
            data: {
                'meal_type': meal_typeId
            },
            success: function (data) {
                $("#id_size").html(data);
            }
        });
        $.ajax({
            url: url_meal_addition,
            data: {
                'meal_type': meal_typeId
            },
            success: function (data) {
                $("#id_meal_addition").html(data);
            }
        });
        var url_price = $("#price").attr("data-price-url");
        $.ajax({
            url: url_price,
            data: {
                'meal_type': meal_typeId,
            },
            success: function () {}
        });
    });
    $("#id_size").change(function () {
        $("#price").show();
        var url_price = $("#price").attr("data-price-url");
        var sizeId = $(this).val();
        $.ajax({
            url: url_price,
            data: {
                'size': sizeId
            },
            success: function (data) {
                $("#price-value").html(data);
            }
        });
        document.getElementById("add-to-basket").disabled = false;
    });
    $("#id_meal_addition").change(function () {
        var url_price = $("#price").attr("data-price-url");
        var meal_additionId = [];
        meal_additionId.push($(this).val());
        console.log(meal_additionId)
        $.ajax({
            url: url_price,
            traditional: true,
            data: {
                'meal_addition': meal_additionId
            },
            success: function () {}
        });
    });
})