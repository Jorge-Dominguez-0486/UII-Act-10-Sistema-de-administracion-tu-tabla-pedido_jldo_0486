

from django import forms
from .models import Pedido 

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
       
        fields = ['pedido_id', 'fecha_hora', 'total_neto', 'metodo_pago', 'estado_pedido'] 

        labels = {
            'pedido_id': 'ID de Pedido',
            'fecha_hora': 'Fecha y Hora del Pedido',
            'total_neto': 'Total Neto',
            'metodo_pago': 'Método de Pago',
            'estado_pedido': 'Estado del Pedido',
        }
        widgets = {
            
            'fecha_hora': forms.DateTimeInput(attrs={'type': 'datetime-local'}), 
            'total_neto': forms.NumberInput(attrs={'step': '0.01'}),
            'metodo_pago': forms.TextInput(attrs={'max_length': 50}),
            'estado_pedido': forms.TextInput(attrs={'max_length': 30}),
        }