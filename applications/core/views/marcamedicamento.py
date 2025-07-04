from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.core.models import MarcaMedicamento
from applications.core.forms.marcamedicamento import MarcaMedicamentoForm

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class MarcamedicamentoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/marcamedicamento/list.html'
    model = MarcaMedicamento
    context_object_name = 'marcas'
    permission_required = 'view_marcamedicamento'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.OR)
           
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:marcamedicamento_create')
        print(context['permissions'])
        return context

class MarcamedicamentoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = MarcaMedicamento
    template_name = 'core/marcamedicamento/form.html'
    form_class = MarcaMedicamentoForm
    success_url = reverse_lazy('core:marcamedicamento_list')
    permission_required = 'add_marcamedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar marca de Medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        marcamedicamento = self.object
        messages.success(self.request, f"Éxito al crear la marca de medicamento {marcamedicamento.nombre}.")
        return response

class MarcamedicamentoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = MarcaMedicamento
    template_name = 'core/marcamedicamento/form.html'
    form_class = MarcaMedicamentoForm
    success_url = reverse_lazy('core:marcamedicamento_list')
    permission_required = 'change_marcamedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar marca de Medicamento'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        marcamedicamento = self.object
        messages.success(self.request, f"Éxito al actualizar la marca Medicamento  {marcamedicamento.nombre}.")
        return response

class MarcamedicamentoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = MarcaMedicamento
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:marcamedicamento_list')
    permission_required = 'delete_marcamedicamento'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar Marca de Medicamento'
        context['description'] = f"¿Desea eliminar la marca de Medicamento: {self.object.name}?"
        context['back_url'] = self.success_url
        return context

    
    def form_valid(self, form):
        # Guardar info antes de eliminar
        marcamedicamento_name = self.object.nombre
        
        # Llamar al delete del padre
        response = super().form_valid(form)
        
        # Agregar mensaje
        messages.success(self.request, f"Éxito al eliminar lógicamente la marca de medicamento { marcamedicamento_name}.")
        
        return response