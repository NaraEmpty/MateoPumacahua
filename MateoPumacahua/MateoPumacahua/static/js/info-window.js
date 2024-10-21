document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.more-info');
    const infoWindow = document.getElementById('info-window');

    buttons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            const id = this.getAttribute('data-id');
            
            fetch(`/asignatura/${id}/`)
                .then(response => response.json())
                .then(data => {
                    fetch('/static/vista_curso.html')
                        .then(response => response.text())
                        .then(html => {
                            html = html.replace('{{ salon }}', data.salon)
                                       .replace('{{ nombre_materia }}', data.nombre_materia);
                            infoWindow.innerHTML = html;
                            infoWindow.classList.add('open');
                        })
                        .catch(error => console.error('Error loading HTML:', error));
                })
                .catch(error => console.error('Error fetching data:', error));
        });
    });
});
