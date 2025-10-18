# app_pedido/views.py


from django.http import HttpResponseRedirect 
from django.shortcuts import render, get_object_or_404 
from django.urls import reverse
from .models import Pedido 
from .forma import PedidoForm # Asegúrate de que este archivo exista

# FUNCIÓN index
def index(request):
    # Consulta todos los pedidos.
    pedidos_data = Pedido.objects.all()
    
    contexto = {
        'Productos': pedidos_data # 'Productos' es la variable que usa index.html
    }
    
    return render(request, 'pedido/index.html', contexto)

# FUNCIÓN view_pedido
def view_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    # Por ahora solo redirige a la lista
    return HttpResponseRedirect(reverse('index')) 

# FUNCIÓN add
def add(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)
        if form.is_valid():
            form.save() 
            return render(request, 'pedido/add.html', {
                'form': PedidoForm(), 
                'success': True       
            })
        else:
            return render(request, 'pedido/add.html', {
                'form': form,
                'success': False
            })
    else:
        form = PedidoForm()
        return render(request, 'pedido/add.html', {
            'form': form,
            'success': False
        })
    
# FUNCIÓN edit
def edit(request, pedido_id): # Acepta pedido_id
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    if request.method == 'POST':
        form = PedidoForm(request.POST, instance=pedido)
        
        if form.is_valid():
            form.save() 
            return render(request, 'pedido/edit.html', {
                'form': form,
                'success': True 
            })
        else:
            return render(request, 'pedido/edit.html', {
                'form': form,
                'success': False
            })
    else:
        form = PedidoForm(instance=pedido)

    return render(request, 'pedido/edit.html', {
        'form': form,
        'success': False
    })

# FUNCIÓN delete
def delete(request, pedido_id): # Acepta pedido_id
    if request.method == 'POST':
        pedido = get_object_or_404(Pedido, pk=pedido_id) 
        pedido.delete()
        return HttpResponseRedirect(reverse('index'))
    
    return HttpResponseRedirect(reverse('index'))