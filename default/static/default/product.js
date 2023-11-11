$("#add_to_cart_btn").click(function(){
    const quantity = parseInt($("#quantity").val())
    const product_id = $("#add_to_cart_btn").data("product-id")
    fetch("/kosar/hozzad/" + product_id + "/" + quantity).then(function(){
        fetch("/kosar/termekek-szama").then(function (response){
            response.json().then(function (response) {
                $("#cart-item-count").text(response)
            })
        })
    })

    const cart_quantity = $("#in_cart_quantity")

    if(cart_quantity.length) {
        cart_quantity.html(parseInt(cart_quantity.html()) + quantity) 
    } else {
        $("#in_cart_placeholder").html("<p style='color: green; font-weight: bold'>Kosárban: <span id='in_cart_quantity'>" + quantity + "</span></p>")
    }

})