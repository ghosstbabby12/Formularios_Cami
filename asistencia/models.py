from django.db import models

class Asistencia(models.Model):
    # Identificación y Contacto
    # Se recomienda max_length=150 o 200 para nombres. Lo mantendremos en 150.
    nombre_completo = models.CharField(
        max_length=150,
        verbose_name='Nombre Completo'  # Mejora el nombre en el Admin y formularios
    )
    # documento puede ser un campo numérico, pero CharField es más flexible para DNIs/Cédulas con letras/guiones.
    documento = models.CharField(
        max_length=50,
        unique=True,  # CRUCIAL: Asegura que no haya documentos duplicados
        verbose_name='Número de Documento'
    )
    # EmailField con el max_length estándar para correos.
    correo = models.EmailField(
        max_length=254,
        verbose_name='Correo Electrónico'
    )

    # Registro de Tiempos
    fecha_asistencia = models.DateField(
        verbose_name='Fecha de Asistencia'
    )
    hora_ingreso = models.TimeField(
        verbose_name='Hora de Ingreso'
    )
    # CRUCIAL: Permitir que hora_salida sea null, ya que el registro se crea al ingresar.
    hora_salida = models.TimeField(
        null=True,
        blank=True,
        verbose_name='Hora de Salida'
    )

    # Estado y Notas
    # El valor por defecto es correcto.
    presente = models.BooleanField(
        default=True,
        verbose_name='¿Estuvo Presente?'
    )
    # verbose_name ayuda a clarificar
    observaciones = models.TextField(
        blank=True,
        null=True,
        verbose_name='Notas u Observaciones'
    )

    # Metaclase para ordenar y mejorar el panel de administración
    class Meta:
        verbose_name = 'Registro de Asistencia'
        verbose_name_plural = 'Registros de Asistencia'
        # Ordena la lista por fecha descendente (más reciente primero)
        ordering = ['-fecha_asistencia', 'hora_ingreso']
        # Evita registros duplicados con la misma fecha y documento
        unique_together = ['documento', 'fecha_asistencia']

    def __str__(self):
        # Devuelve el nombre completo y la fecha para una mejor identificación en el Admin
        return f'{self.nombre_completo} ({self.fecha_asistencia})'