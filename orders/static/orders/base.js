document.addEventListener("DOMContentLoaded", () => {

    $("#id_meal").change(function () {
        var url = $("#orderForm").attr("data-meal_types-url");
        var mealId = $(this).val();

        $.ajax({
            url: url,
            data: {
                'meal': mealId
            },
            success: function (data) {
                $("#id_meal_type").html(data);
            }
        });
    });
})