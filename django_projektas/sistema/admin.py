from django.contrib import admin
from restoranai.models import Restoranas
from darbuotojai.models import Darbuotojas
from sales.models import Sale
from stalai.models import Stalas


admin.site.register(Restoranas)
admin.site.register(Darbuotojas)
admin.site.register(Sale)
admin.site.register(Stalas)
