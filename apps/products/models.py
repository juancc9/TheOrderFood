from django.db import models

class Product(models.Model):
    adiciones = [
        ('sal','Sal'),
        ('salTo','Salsa_Tomate'),
        ('mayo','Mayonesa'),
        ('salRo','Salsa_Rosada'),
        ('salPi','Salsa_Piña'),
        ('N','Ninguna'),


    ]

   
    name = models.CharField(max_length=50)
    adicion = models.CharField(max_length=20,choices=adiciones)
    description = models.TextField()
    def __str__(self):
        return self.name

class Orden(models.Model):
    Tipo_de_Ordenes = [
        ('pa_ll','pa llevar'),
        ('pa_cm','para comer aqui'),
        ('pa_dm','para Domicilio')

    ]
    estados = [
        ('esp','En espera'),
        ('pre','En Preparacion'),
        ('serv','Plato Servido')
    ]
    NombreOrden = models.CharField(max_length=40,null=True)
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    Cantidad = models.IntegerField()
    Tipo_Orden= models.CharField(max_length=20,choices=Tipo_de_Ordenes)
    estado = models.CharField(max_length=20,choices=estados,default='esp')
    date = models.DateField(auto_now=True)