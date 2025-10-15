
# app_proveedor/models.py

from django.db import models

class Proveedor(models.Model):
    # El 'id' se crea automáticamente por Django
    nombre = models.CharField(max_length=50)
    ap_paterno = models.CharField(max_length=50)
    ap_materno = models.CharField(max_length=50)
    categoria = models.CharField(max_length=100)
    contacto = models.CharField(max_length=15) # Usamos CharField para números de contacto

    class Meta:
        # Se establece el nombre de la tabla en la base de datos
        db_table = 'proveedor'

    def __str__(self):
        # Representación en texto para el panel de administración
        return f'{self.nombre} {self.ap_paterno} - {self.categoria}'