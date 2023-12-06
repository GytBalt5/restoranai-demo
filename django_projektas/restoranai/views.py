from django.db import models


class Restoranas(models.Model):
    pavadinimas = models.CharField(max_length=100, verbose_name="Pavadinimas")
    adresas = models.CharField(max_length=200, verbose_name="Adresas")
    telefonas = models.CharField(max_length=20, verbose_name="Telefonas")
    el_pastas = models.EmailField(verbose_name="El. paštas")
    atidarymo_valandos = models.TextField(verbose_name="Atidarymo valandos")

    def __str__(self):
        return self.pavadinimas
