$(document).ready(function () {
    // Selecciona el menú offcanvas
    var offcanvasElement = document.getElementById('offcanvasNavbar');
    
    // Crear una instancia de Offcanvas de Bootstrap
    var bsOffcanvas = new bootstrap.Offcanvas(offcanvasElement);

    // Manejar clics en enlaces dentro del offcanvas
    $('#offcanvasNavbar .nav-link').on('click', function () {
        var target = $(this).attr('href'); // Obtén el objetivo del enlace
        // Navega a la sección objetivo
        $('html, body').animate({
            scrollTop: $(target).offset().top
        }, 500, function () {
            // Cierra el offcanvas después de un breve retraso
            setTimeout(function () {
                bsOffcanvas.hide();
            }, 300); // Ajusta el retraso según sea necesario
        });
    });
});
