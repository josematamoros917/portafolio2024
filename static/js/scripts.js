document.addEventListener('DOMContentLoaded', function() {
    // Obtener todos los enlaces dentro del menú offcanvas
    const menuLinks = document.querySelectorAll('#offcanvasNavbar .nav-link');
    
    // Añadir un event listener a cada enlace
    menuLinks.forEach(link => {
        link.addEventListener('click', () => {
            // Cerrar el menú offcanvas al hacer clic en un enlace
            const offcanvas = document.getElementById('offcanvasNavbar');
            const bsOffcanvas = bootstrap.Offcanvas.getInstance(offcanvas);
            if (bsOffcanvas) {
                bsOffcanvas.hide();
            }
        });
    });
});
