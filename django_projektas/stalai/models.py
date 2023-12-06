from django.db import models


class Stalas(models.Model):
    numeris = models.IntegerField(verbose_name="Numeris", unique=True)
    vietu_skaicius = models.IntegerField(verbose_name="Vietų skaičius")
    uzsakymas = models.BooleanField(default=False, verbose_name="Užsakytas")

    sale = models.ForeignKey(
        to="sales.Sale",
        on_delete=models.CASCADE,
        verbose_name="Salė",
        related_name="stalai",
    )
    darbuotojas = models.ForeignKey(
        to="darbuotojai.Darbuotojas",
        on_delete=models.CASCADE,
        verbose_name="Darbuotojas",
        related_name="stalai",
    )
