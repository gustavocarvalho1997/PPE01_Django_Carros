from django.db import models

# Create your models here.
class Car(models.Model):
    # Atributos
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    value = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    # Método para retornar o nome do modelo
    def __str__(self):
        return self.model