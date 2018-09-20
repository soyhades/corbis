from django.shortcuts import render
from .forms import ProductoForm
from .models import Producto

def home(request):
    template_name = 'home.html'
    lista_productos =Producto.objects.all()
    if request.method == 'POST':
        id_producto = request.POST.get('id','0')
            if id_producto =='0':
                form = ProductoForm(request.POST)
            else:
                producto= Producto.objects.get(id=id_producto)
                form =ProductoForm (
                        request.POST, instanse=producto
                        )

            if form.is_valid():
                form.save()
            else
                form = ProductoForm()

            return render(
            request,
            template_name
                {
                    'form': form,
                    'lista_productos': lista_productos
                }
            )
