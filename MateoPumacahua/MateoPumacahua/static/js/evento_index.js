document.addEventListener('DOMContentLoaded', function() {
    const prevButton = document.querySelector('.prev');
    const nextButton = document.querySelector('.next');
    const eventos = document.querySelectorAll('.evento');
    let currentIndex = 0;

    function showEvent(index) {
        eventos.forEach((evento, i) => {
            evento.classList.toggle('active', i === index);
        });
    }

    prevButton.addEventListener('click', function() {
        currentIndex = (currentIndex > 0) ? currentIndex - 1 : eventos.length - 1;
        showEvent(currentIndex);
    });

    nextButton.addEventListener('click', function() {
        currentIndex = (currentIndex < eventos.length - 1) ? currentIndex + 1 : 0;
        showEvent(currentIndex);
    });

    // Mostrar el primer evento al cargar la página
    showEvent(currentIndex);
});
