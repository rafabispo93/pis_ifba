from django.contrib import admin

# Register your models here.
from .models import Projeto, Profissional

admin.site.register(Projeto)
admin.site.register(Profissional)
