from django.contrib import admin
from django.contrib.auth.hashers import make_password
from .models import Entrada, Alumno, Profesor, Asignatura, Calificacion, Salon, HistoricalReview
from .forms import AlumnoForm, ProfesorForm

@admin.register(Entrada)
class EntradaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('nombre', 'contenido')
    list_filter = ('tipo', 'fecha_creacion')

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    form = AlumnoForm
    list_display = ('codigo', 'nombre_completo', 'correo', 'telefono', 'salon')
    search_fields = ('codigo', 'nombre_completo', 'correo')

    def save_model(self, request, obj, form, change):
        if not obj.pk or (obj.pk and obj.password != Alumno.objects.get(pk=obj.pk).password):
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    form = ProfesorForm
    list_display = ('codigo', 'nombre_completo', 'correo', 'telefono', 'salon')
    search_fields = ('codigo', 'nombre_completo', 'correo')

    def save_model(self, request, obj, form, change):
        if not obj.pk or (obj.pk and obj.password != Profesor.objects.get(pk=obj.pk).password):
            obj.password = make_password(obj.password)
        super().save_model(request, obj, form, change)

@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre_materia', 'salon')
    search_fields = ('nombre_materia', 'salon__codigo')

@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ('calificacion', 'alumno', 'asignatura')
    search_fields = ('alumno__nombre_completo', 'asignatura__nombre_materia')

@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'grado', 'seccion')
    search_fields = ('codigo', 'grado', 'seccion')


class HistoricalReviewAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'content')

admin.site.register(HistoricalReview, HistoricalReviewAdmin)
