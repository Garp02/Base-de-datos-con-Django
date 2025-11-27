from django.shortcuts import render
from .models import Sistemascomputo
from .forms import ComputadoraForm

# Visualizar 
def lista_computadoras(request):

    computadoras = Sistemascomputo.objects.all()
    
    return render(request, 'lista.html', {'computadoras': computadoras})

# Agregar
def agregar_computadora(request):

    if request.method == 'POST':
    
        form = ComputadoraForm(request.POST)
    
        if form.is_valid():
    
            form.save()
    
            return redirect('lista_computadoras')
    else:
    
        form = ComputadoraForm()
    
    return render(request, 'formulario.html', {'form': form, 'accion': 'Agregar'})

# Editar
def editar_computadora(request, id):

    computadora = get_object_or_404(Sistemascomputo, id = id)
    
    if request.method == 'POST':
        
        form = ComputadoraForm(request.POST, instance = computadora)
        
        if form.is_valid():
        
            form.save()
        
            return redirect('lista_computadoras')
    
    else:
    
        form = ComputadoraForm(instance = computadora)
    
    return render(request, 'formulario.html', {'form': form, 'accion': 'Editar'})

# Borrar
def borrar_computadora(request, id):

    computadora = get_object_or_404(Sistemascomputo, id = id)
    
    if request.method == 'POST':
    
        computadora.delete()
    
        return redirect('lista_computadoras')
    
    return render(request, 'confirmar_borrar.html', {'computadora': computadora})