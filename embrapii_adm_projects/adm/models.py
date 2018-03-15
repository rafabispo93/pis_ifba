# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

class Profissional(models.Model):
    cargo = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(
            default=timezone.now)
    custo = models.FloatField()
    carga_horaria = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return self.cargo

class Projeto(models.Model):
    nome =  models.CharField(max_length=200)
    descricao = models.TextField(default=None)
    data_criacao = models.DateTimeField(
            default=timezone.now)
    profissionais = models.ManyToManyField(Profissional)

    def __str__(self):
        return self.nome
