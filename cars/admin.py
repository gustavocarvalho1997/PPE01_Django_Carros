from django.contrib import admin
from cars.models import Car

# Register your models here.
# Classes de configuração do admin
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'brand', 'factory_year', 'model_year', 'value')
    search_fields = ('model', 'brand')


# Registra o model no admin
admin.site.register(Car, CarAdmin)
