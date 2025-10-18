from django.db import models

class Pedido(models.Model):
    
    pedido_id = models.AutoField(
        primary_key=True,
        unique=True,
        verbose_name="ID de Pedido"
    )

    
    fecha_hora = models.DateTimeField(
       
        verbose_name="Fecha y Hora del Pedido"
    )

    
    total_neto = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Total Neto"
    )

    
    metodo_pago = models.CharField(
        max_length=50,
        verbose_name="Método de Pago"
    )

   
    estado_pedido = models.CharField(
        max_length=30,
        default='Pendiente',
        verbose_name="Estado del Pedido"
    )

    class Meta:
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"
        ordering = ['-fecha_hora']

    def __str__(self):
        return f"Pedido N° {self.pedido_id} - {self.fecha_hora.strftime('%Y-%m-%d')}"