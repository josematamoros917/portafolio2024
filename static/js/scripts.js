$(document).ready(function () {
    // Selecciona el menú offcanvas
    var offcanvasElement = document.getElementById('offcanvasNavbar');
    
    // Crear una instancia de Offcanvas de Bootstrap
    var bsOffcanvas = new bootstrap.Offcanvas(offcanvasElement);

    // Manejar clics en enlaces dentro del offcanvas
    $('#offcanvasNavbar .nav-link').on('click', function () {
        bsOffcanvas.hide(); // Cierra el offcanvas
    });
});
