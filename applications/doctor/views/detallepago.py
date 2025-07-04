from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.doctor.models import DetallePago, Pago
from applications.doctor.forms.detallepago import DetallePagoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q


from django.views.generic import DetailView
from django.urls import reverse_lazy

class PagoDetailView(PermissionMixin, DetailView):
    model = Pago
    template_name = 'doctor/pagos/detail.html'
    context_object_name = 'pago'
    permission_required = 'view_pago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pago = self.object
        context['detalle_pagos'] = pago.detalles.all().order_by('id')
        context['title1'] = f"Detalle de Pago {pago.id}"
        context['back_url'] = reverse_lazy('doctor:pagos_list')
        return context


