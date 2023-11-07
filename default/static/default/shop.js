$(document).ready(function() {
    $("#szuro").on("change",function() {
        document.location.href = "/aruhaz/kategoriak/" + $("#szuro").val() + "#termekek"
    })
})