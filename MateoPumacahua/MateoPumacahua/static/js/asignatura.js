document.getElementById('asignaturas-link').addEventListener('click', function(event) {
    event.preventDefault();
    fetch('/asignaturas/')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el contenido');
            }
            return response.text();
        })
        .then(data => {
            document.querySelector('.contenido').innerHTML = data;
        })
        .catch(error => console.error('Error al cargar el contenido:', error));
});
