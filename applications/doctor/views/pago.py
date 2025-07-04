from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.doctor.models import Pago
from applications.doctor.forms.pago import PagoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from applications.doctor.formsets import DetallePagoFormSet


class PagoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'doctor/pagos/list.html'
    model = Pago
    context_object_name = 'pagos'
    permission_required = 'view_pago'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.OR)
           
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('doctor:pagos_create')
        print(context['permissions'])
        return context

class PagoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Pago
    form_class = PagoForm
    template_name = 'doctor/pagos/form.html'
    success_url = reverse_lazy('doctor:pagos_list')
    permission_required = 'add_pago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = DetallePagoFormSet(self.request.POST, prefix='detalles')
        else:
            context['formset'] = DetallePagoFormSet(prefix='detalles')
        context['grabar'] = 'Grabar Pago'
        context['back_url'] = self.success_url
        return context
       
    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if formset.is_valid():
            self.object = form.save()
            formset.instance = self.object
            formset.save()

            # Captura del ID de PayPal si fue seleccionado
            if form.cleaned_data['metodo_pago'] == 'Paypal':
                txn_id = self.request.POST.get('paypal_transaction_id')
                if txn_id:
                    print(f"[DEBUG] Transacción simulada PayPal ID: {txn_id}")
                    # Puedes guardar esto en tu modelo si quieres persistirlo.

            messages.success(self.request, "Pago registrado correctamente.")
            return super().form_valid(form)
        else:
            print("Formset inválido:")
            print(formset.errors)
            print(formset.non_form_errors())
            return self.render_to_response(self.get_context_data(form=form))

class PagoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Pago
    form_class = PagoForm
    template_name = 'doctor/pagos/form.html'
    success_url = reverse_lazy('doctor:pagos_list')
    permission_required = 'change_pago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['formset'] = DetallePagoFormSet(self.request.POST, instance=self.object, prefix='detalles')
        else:
            context['formset'] = DetallePagoFormSet(instance=self.object, prefix='detalles')
        context['grabar'] = 'Actualizar Pago'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        
        if formset.is_valid():
            self.object = form.save()                    
            formset.instance = self.object                
            formset.save()                               
            messages.success(self.request, "Pago actualizado correctamente.")
            return super().form_valid(form)
        else:
            print("Formset inválido:")
            print(formset.errors)
            print(formset.non_form_errors())
            return self.render_to_response(self.get_context_data(form=form))



class PagoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Pago
    template_name = 'doctor/delete.html'
    success_url = reverse_lazy('doctor:pagos_list')
    permission_required = 'delete_pago'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Pagos'
        context['description'] = f"¿Desea eliminar el Pago: {self.object.atencion}?"
        context['back_url'] = self.success_url
        return context

    
    def form_valid(self, form):
        # Guardar info antes de eliminar
        pagos_name = self.object.atencion
        
        # Llamar al delete del padre
        response = super().form_valid(form)
        
        # Agregar mensaje
        messages.success(self.request, f"Éxito al eliminar lógicamente el Pagos {pagos_name}.")
        
        return response