$(".remove-cart-btn").click(function () {
    let product_id = $(this).data("product-id")

    fetch("/kosar/eltavolit/" + product_id).then(function (response){
        response.json().then(function (response) {
            $("#total-price").text(response + " FT")
            $("#product-" + product_id).remove()
        }
        )
    })
})