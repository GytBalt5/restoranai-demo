from django.db import models


class Darbuotojas(models.Model):
    vardas = models.CharField(max_length=100, verbose_name="Vardas")
    pareigos = models.CharField(max_length=100, verbose_name="Pareigos")
    el_pastas = models.EmailField(verbose_name="El. paštas")
    isdarbinimo_data = models.DateField(verbose_name="Įdarbinimo data")

    restoranas = models.ForeignKey(
        to="restoranai.Restoranas", 
        on_delete=models.CASCADE, 
        verbose_name="Restoranas",
    )

    def __str__(self):
        return self.vardas
