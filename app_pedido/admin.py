from django.contrib import admin
from .models import Pedido 


class PedidoAdmin(admin.ModelAdmin):
    list_display = (
        'pedido_id', 
        'fecha_hora', 
        'total_neto', 
        'metodo_pago', 
        'estado_pedido',
    )
    list_filter = ('estado_pedido', 'metodo_pago')
    search_fields = ('pedido_id', 'metodo_pago')


admin.site.register(Pedido, PedidoAdmin)