$(document).ready(function() {
    $("#szuro").on("change",function() {
        document.location.href = "/aruhaz/kategoriak/" + $("#szuro").val() + "#termekek"
    })

    $(".add_to_cart_btn").click(function(){
        fetch("/kosar/hozzad/" + $(this).data("product-id") + "/1")
    })
})