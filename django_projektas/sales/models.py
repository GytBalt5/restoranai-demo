from django.db import models


class Sale(models.Model):
    pavadinimas = models.CharField(max_length=100)
    talpa = models.IntegerField()
    rezervuota = models.BooleanField(default=False)

    restoranas = models.ForeignKey(
        to="restoranai.Restoranas", 
        on_delete=models.CASCADE,
        verbose_name="Restoranas",
        related_name="sales",
    )
