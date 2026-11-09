from django.db import models

# ---------- Modelo Categoría ----------
class Responsable(models.Model):
    nombre = models.CharField(max_length=100, null=False)
    correo = models.CharField(max_length=100,unique=True,null=False)
    rut = models.CharField(max_length=20)
    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Responsables"
        ordering = ["nombre"]



class Mascota (models.Model):
    nombre = models.CharField(max_length=100,null=False)
    anio_nacimiento = models.IntegerField(null=False)
    especie = models.CharField(max_length=100,null=False)
    responsable = models.ForeignKey(Responsable, on_delete=models.CASCADE,null=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Mascotas"
        ordering = ["nombre"]


# ---------- Modelo Producto ----------


