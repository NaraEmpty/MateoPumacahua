/*document.addEventListener('DOMContentLoaded', function() {
    const tipoClienteField = document.querySelector('#id_tipo_cliente');
    const nivelField = document.querySelector('.field-nivel');
    const gradoYSeccionField = document.querySelector('.field-grado_y_seccion');
    const tutorField = document.querySelector('.field-tutor');
    const asignaturaField = document.querySelector('.field-asignatura');

    function toggleFields() {
        const tipoCliente = tipoClienteField.value;
        if (tipoCliente === '1') {  // Alumno
            nivelField.style.display = 'block';
            gradoYSeccionField.style.display = 'block';
            tutorField.style.display = 'block';
            asignaturaField.style.display = 'none';
        } else if (tipoCliente === '3') {  // Profesor
            nivelField.style.display = 'none';
            gradoYSeccionField.style.display = 'none';
            tutorField.style.display = 'none';
            asignaturaField.style.display = 'block';
        } else {
            nivelField.style.display = 'none';
            gradoYSeccionField.style.display = 'none';
            tutorField.style.display = 'none';
            asignaturaField.style.display = 'none';
        }
    }

    tipoClienteField.addEventListener('change', toggleFields);
    toggleFields();  // Inicializar la visualización de los campos
});*/
