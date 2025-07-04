from django.contrib import messages
from django.urls import reverse_lazy
from applications.security.components.mixin_crud import CreateViewMixin, DeleteViewMixin, ListViewMixin, PermissionMixin, UpdateViewMixin
from applications.core.models import Diagnostico
from applications.core.forms.diagnostico import DiagnosticoForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q

class DiagnosticoListView(PermissionMixin, ListViewMixin, ListView):
    template_name = 'core/diagnostico/list.html'
    model = Diagnostico
    context_object_name = 'diagnostico'
    permission_required = 'view_diagnostico'

    def get_queryset(self):
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(name__icontains=q1), Q.OR)
           
        return self.model.objects.filter(self.query).order_by('id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_url'] = reverse_lazy('core:diagnostico_create')
        print(context['permissions'])
        return context

class DiagnosticoCreateView(PermissionMixin, CreateViewMixin, CreateView):
    model = Diagnostico
    template_name = 'core/diagnostico/form.html'
    form_class = DiagnosticoForm
    success_url = reverse_lazy('core:diagnostico_list')
    permission_required = 'add_diagnostico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Diagnostico'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        tipogasto = self.object
        messages.success(self.request, f"Éxito al crear el Diagnostico {tipogasto.codigo}.")
        return response

class DiagnosticoUpdateView(PermissionMixin, UpdateViewMixin, UpdateView):
    model = Diagnostico
    template_name = 'core/diagnostico/form.html'
    form_class = DiagnosticoForm
    success_url = reverse_lazy('core:diagnostico_list')
    permission_required = 'change_diagnostico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Diagnostico'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        tipogasto = self.object
        messages.success(self.request, f"Éxito al actualizar el diagnostico {tipogasto.codigo}.")
        return response

class DiagnosticoDeleteView(PermissionMixin, DeleteViewMixin, DeleteView):
    model = Diagnostico
    template_name = 'core/delete.html'
    success_url = reverse_lazy('core:diagnostico_list')
    permission_required = 'delete_diagnostico'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Eliminar diagnostico'
        context['description'] = f"¿Desea eliminar el diagnostico: {self.object.name}?"
        context['back_url'] = self.success_url
        return context

    
    def form_valid(self, form):
        # Guardar info antes de eliminar
        diagnostico_name = self.object.codigo
        
        # Llamar al delete del padre
        response = super().form_valid(form)
        
        # Agregar mensaje
        messages.success(self.request, f"Éxito al eliminar lógicamente el diagnostico {diagnostico_name}.")
        
        return response