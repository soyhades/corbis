from django.models import ModelForm
from models import producto

class ProductoForm(ModelForm)
    class Meta:
        model = producto
        exlude = ['fecha',]
        field = ['codigo','nombre','cantidad']
