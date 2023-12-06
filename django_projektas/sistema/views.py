from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from darbuotojai.models import Darbuotojas
from sales.models import Sale
from stalai.models import Stalas


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        # Gaunami konteksto duomenys iš bazinės klasės.
        context = super().get_context_data(**kwargs)

        # Įtraukiama papildoma informacija į kontekstą.
        context['sales'] = Sale.objects.all()
        context['darbuotojai'] = Darbuotojas.objects.all()
        context['stalai'] = Stalas.objects.all()

        return context

    def post(self, request, *args, **kwargs):
        # Gaunami POST užklausos parametrai.
        pasirinktas_darbuotojas_id = request.POST.get('darbuotojas')
        pasirinkta_sale_id = request.POST.get('sale')

        # Filtravimas pagal pasirinktus parametrus.
        stalai = Stalas.objects.all()
        if pasirinktas_darbuotojas_id:
            stalai = stalai.filter(darbuotojas_id=pasirinktas_darbuotojas_id)
        if pasirinkta_sale_id:
            stalai = stalai.filter(sale_id=pasirinkta_sale_id)

        # Saugus objektų gavimas; jei objektas nerastas, bus grąžinamas None.
        pasirinktas_darbuotojas = get_object_or_404(Darbuotojas, id=pasirinktas_darbuotojas_id) if pasirinktas_darbuotojas_id else None
        pasirinkta_sale = get_object_or_404(Sale, id=pasirinkta_sale_id) if pasirinkta_sale_id else None

        # Atnaujinamas kontekstas su filtruotais duomenimis.
        context = self.get_context_data()
        context.update({
            'pasirinktas_darbuotojas': pasirinktas_darbuotojas,
            'pasirinkta_sale': pasirinkta_sale,
            'stalai': stalai,
        })
        
        return self.render_to_response(context)
