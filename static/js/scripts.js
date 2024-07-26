$(document).ready(function () {
    var offcanvasElement = document.getElementById('offcanvasNavbar');
    var bsOffcanvas = new bootstrap.Offcanvas(offcanvasElement);

    $('#offcanvasNavbar .nav-link').on('click', function (event) {
        event.preventDefault();
        var target = $(this).attr('href');
        
        $('html, body').animate({
            scrollTop: $(target).offset().top - 100 // Ajusta este valor según el tamaño de tu navbar
        }, 500, function () {
            setTimeout(function () {
                bsOffcanvas.hide();
            }, 300);
        });
    });
});
