var header_util = {
    mobileMenu() {
      $("#nav").toggleClass("nav-visible");
    },
    windowResize() {
      if ($(window).width() > 1000) {
        $("#nav").removeClass("nav-visible");
      }
    }
}

$(document).ready(function() {
    $("#menu").click(header_util.mobileMenu);
    $(window).resize(header_util.windowResize);
})