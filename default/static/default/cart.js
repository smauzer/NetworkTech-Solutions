$(".remove-cart-btn").click(function () {
    let product_id = $(this).data("product-id")

    fetch("/kosar/eltavolit/" + product_id).then(function (response){
        response.json().then(function (response) {
            $("#total-price").text(response + " Ft")
            $("#product-" + product_id).remove()
        })
    })
})

$(".product-quantity").change(function () {
    const previous_quantity = $(this).data("previous-quantity")
    const new_quantity = $(this).val()

    const dif = new_quantity - previous_quantity

    if (previous_quantity + dif <= 0) {
        $("#product-" + $(this).data("product-id")).remove()
    }

    fetch("/kosar/hozzad/" + $(this).data("product-id") + "/"  + dif).then(function (response){
        response.json().then(function (response) {
            $("#total-price").text(response + " Ft")
        })
    })

    $(this).data("previous-quantity", new_quantity)
})