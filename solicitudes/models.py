from django.db import models

class Solicitud(models.Model):
    TIPO_SOLICITUD = [
        ('academica', 'Académica'),
        ('administrativa', 'Administrativa'),
        ('tecnica', 'Técnica'),
        ('otra', 'Otra'),
    ]

    nombre_solicitante = models.CharField(max_length=150)
    documento = models.CharField(max_length=50)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20, choices=TIPO_SOLICITUD)
    asunto = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha = models.DateField()
    archivo = models.FileField(upload_to='uploads/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"
