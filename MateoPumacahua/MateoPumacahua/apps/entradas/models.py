from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model

# Definición de las opciones de género
GENERO_CHOICES = [
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
]

# Modelo para las entradas
class Entrada(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    TIPOS_CHOICES = [
        ('1', 'Personaje'),
        ('2', 'Lugar'),
        ('3', 'Objeto'),
        ('4', 'Evento'),
    ]
    tipo = models.CharField(max_length=1, choices=TIPOS_CHOICES, verbose_name="Tipo")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_modificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de modificación")
    imagen = models.ImageField(upload_to='entradas/', null=True, blank=True, verbose_name="Imagen")
    contenido = CKEditor5Field(verbose_name="Contenido")

    def guardar_imagen(self, imagen):
        if self.imagen:
            self.imagen.delete()
        return imagen



# Modelo para Alumno
class Alumno(models.Model):
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código")
    nombre_completo = models.CharField(max_length=255)
    correo = models.EmailField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    telefono = models.CharField(max_length=15)
    password = models.CharField(max_length=255)
    salon = models.ForeignKey('Salon', on_delete=models.CASCADE, related_name='alumnos')

    def clean(self):
        if not self.salon:
            raise ValidationError("El campo 'salon' es obligatorio para los alumnos.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Alumno"
        verbose_name_plural = "Alumnos"

# Modelo para Profesor
class Profesor(models.Model):
    codigo = models.CharField(max_length=10, unique=True, verbose_name="Código")
    nombre_completo = models.CharField(max_length=255)
    correo = models.EmailField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    telefono = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?1?\d{9}$', message="El número de teléfono debe estar en el formato: '+999999999'. Hasta 15 dígitos permitidos.")
    ])
    password = models.CharField(max_length=255)
    salon = models.ForeignKey('Salon', on_delete=models.CASCADE, related_name='profesores')

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"


#prueba
class Modelo_Usuario(models.Model):
    nombres = models.CharField(max_length=255)
    apellido_paterno = models.CharField(max_length=255)
    apellido_materno = models.CharField(max_length=255)
    correo = models.EmailField()
    genero = models.CharField(max_length=10, choices=GENERO_CHOICES)
    telefono = models.CharField(max_length=15, validators=[
        RegexValidator(regex=r'^\+?1?\d{9}$', message="El número de teléfono debe estar en el formato: '+999999999'. Hasta 9 dígitos permitidos.")
    ])
    contraseña = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre_completo
    
    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

# Modelo para Asignatura
class Asignatura(models.Model):
    nombre_materia = models.CharField(max_length=255, verbose_name="Nombre de la Materia")
    salon = models.ForeignKey('Salon', on_delete=models.CASCADE, related_name='asignaturas')
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name='asignaturas')

    def __str__(self):
        return self.nombre_materia

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

# Modelo para Calificación
class Calificacion(models.Model):
    calificacion = models.FloatField(verbose_name="Calificación")
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE, related_name="calificaciones", verbose_name="Alumno")
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE, related_name="calificaciones", verbose_name="Asignatura")

    def __str__(self):
        return f"{self.alumno.nombre_completo} - {self.asignatura.nombre_materia}: {self.calificacion}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"

# Modelo para Salon
class Salon(models.Model):
    codigo = models.CharField(max_length=255, unique=True, verbose_name="Código del Salón")
    grado = models.CharField(max_length=50, verbose_name="Grado")
    seccion = models.CharField(max_length=50, verbose_name="Sección")

    def __str__(self):
        return f"{self.codigo} - {self.grado} - {self.seccion}"

    class Meta:
        verbose_name = "Salón"
        verbose_name_plural = "Salones"





class EmailBackend(BaseBackend):
    def authenticate(self, request, correo=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(EmailBackend=correo)
        except UserModel.DoesNotExist:
            return None

        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None

class HistoricalReview(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image1 = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
