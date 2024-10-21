from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from apps.entradas.views import (
    index,
    EntradaListView,
    AlumnoListView, 
    detalle_alumno, 
    ProfesorListView, 
    detalle_profesor,
    asignatura,  # Asegúrate de importar la vista 'asignatura'
    CustomLoginView,
    lista_asignaturas,  # Importa la vista lista_asignaturas
    historical_review_view,
    asignatura_detail
)

urlpatterns = [
    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('ckeditor5/', include('django_ckeditor_5.urls')),  # URL para el editor CKEditor

    # Vista index que muestra la lista de entradas
    path('', EntradaListView.as_view(), name='index'),  

    # URL para la vista index que renderiza index.html
    path('index/', index, name='index_html'),

    # Vista de login
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index'), name='logout'),

    # Vista para listar alumnos
    path('alumnos/', AlumnoListView.as_view(), name='alumnos'),

    # Vista para mostrar los detalles de un alumno específico
    path('alumno/<int:id>/', detalle_alumno, name='detalle_alumno'),

    # Vista para listar profesores
    path('profesores/', ProfesorListView.as_view(), name='profesores'),

    # Vista para mostrar los detalles de un profesor específico
    path('profesor/<int:id>/', detalle_profesor, name='detalle_profesor'),

    # Vista del curso "Calidad del Software"
    path('asignatura/<int:id>/', asignatura_detail, name='asignatura_detail'),

    # Incluye las URLs de autenticación de Django
    path('accounts/', include('django.contrib.auth.urls')),
    

    # Vista de cierre de sesión (esto ya está incluido en 'accounts/')
    # path('logout/', include('django.contrib.auth.urls')),  # No es necesario incluirlo de nuevo
    
    # Para que el alumno vea las asignaturas que tiene
    path('asignaturas/', lista_asignaturas, name='lista_asignaturas'),


    path('historia-review/', historical_review_view, name='historia'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Configuración para servir archivos estáticos en desarrollo
