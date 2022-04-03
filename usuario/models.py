from django.db import models
from pandas import notnull

class Usuario(models.Model):
    username = models.CharField(max_length=45,default='teste')
    ticker = models.CharField(max_length=450, default= 'B3SA3.SA')
    tempomonitoramento = models.IntegerField(default='1')
    iniciomonitoramentoemdias = models.IntegerField(default='1')
    terminomonitoramentoemdias = models.IntegerField(default='1')
    email = models.CharField(max_length=100,default='teste@teste.com')
    valormenor = models.DecimalField(max_digits=9, decimal_places=2, default='100')
    valormaior = models.DecimalField(max_digits=9, decimal_places=2, default='1')



# Create your models here.
