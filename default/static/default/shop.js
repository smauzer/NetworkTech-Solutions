$(document).ready(function() {
    $("#szuro").on("change",function() {
        document.location.href = "/aruhaz/kategoriak/" + $("#szuro").val() + "#termekek"
    })

    $(".add_to_cart_btn").click(function(){
        fetch("/kosar/hozzad/" + $(this).data("product-id") + "/1").then(function(){
            fetch("/kosar/termekek-szama").then(function (response){
                response.json().then(function (response) {
                    $("#cart-item-count").text(response)
                })
            })
        })
    })
})