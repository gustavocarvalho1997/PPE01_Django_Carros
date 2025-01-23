from django import forms
from cars.models import Brand
from cars.models import Car

class CarForm(forms.Form):
    model = forms.CharField(label='Modelo', max_length=200)
    brand = forms.ModelChoiceField(label='marca', queryset=Brand.objects.all())
    factory_year = forms.IntegerField(label='Ano de Fabricação', required=False)
    model_year = forms.IntegerField(label='Ano do Modelo', required=False)
    plate = forms.CharField(label='Placa', max_length=10, required=False)
    value = forms.DecimalField(label='Valor', max_digits=10, decimal_places=2, required=False)
    photo = forms.ImageField(label='Foto', required=False)

    def save(self):
        car = Car(
            model = self.cleaned_data['model'],
            brand = self.cleaned_data['brand'],
            factory_year = self.cleaned_data['factory_year'],
            model_year = self.cleaned_data['model_year'],
            plate = self.cleaned_data['plate'],
            value = self.cleaned_data['value'],
            photo = self.cleaned_data['photo']
        )
        car.save()
        return car