document.getElementById('historia-link').addEventListener('click', function(event) {
    event.preventDefault();
    fetch('vista principal/Historia.html')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el contenido');
            }
            return response.text();
        })
        .then(data => {
            document.querySelector('#dynamic-content').innerHTML = data;
        })
        .catch(error => console.error('Error al cargar el contenido:', error));
});
