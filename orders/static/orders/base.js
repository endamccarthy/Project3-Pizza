document.addEventListener("DOMContentLoaded", () => {

    // order page dropdown menu functionality
    $("#id_meal").change(function () {
        var url_meal_type = $("#orderForm").attr("data-meal_type-url");
        var mealId = $(this).val();
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
    });

})