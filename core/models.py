from tkinter import CASCADE
from django.db import models

from users.models import CustomUser

class Notes(models.Model):
    vehicle_model = models.CharField('Titulo', max_length=100, null=False, help_text="ex: Corsa")
    plate = models.CharField('Placa', max_length=8, null=False, unique=True)
    total_value = models.DecimalField('Valor total', decimal_places=2, max_digits=8, default=0)
    creator_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    situation = models.CharField('Situação', max_length=20, null=True)

class Items(models.Model):
    description = models.CharField('Descrição', max_length=100, null=False, help_text="Descrição do serviço ou peça")
    value = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE)

class Observation(models.Model):
    observation = models.CharField('Observação', max_length=250, null=True)
    note = models.ForeignKey(Notes, on_delete=models.CASCADE)


