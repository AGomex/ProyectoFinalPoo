import re
from django import forms
from django.forms import ModelForm

from applications.core.models import Medicamento

class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            'tipo',
            'marca_medicamento',
            'nombre',
            'descripcion',
            'concentracion',
            'via_administracion',
            'cantidad',
            'precio',
            'comercial',
            'foto',
            'activo',
        ]
        labels = {
            'tipo': "Tipo de Medicamento",
            'marca_medicamento': "Marca",
            'nombre': "Nombre",
            'descripcion': "Descripción",
            'concentracion': "Concentración",
            'via_administracion': "Vía de Administración",
            'cantidad': "Cantidad",
            'precio': "Precio",
            'comercial': "¿Es comercial?",
            'foto': "Foto",
            'activo': "Activo",
        }
        error_messages = {
            "nombre": {
                "unique": "Ya existe un medicamento con este nombre.",
            }
        }
        widgets = {
            "tipo": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "marca_medicamento": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "nombre": forms.TextInput(attrs={
                "placeholder": "Ej: Ibuprofeno",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "descripcion": forms.Textarea(attrs={
                "rows": 3,
                "placeholder": "Uso, indicaciones o precauciones relevantes.",
                "id": "id_descripcion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "concentracion": forms.TextInput(attrs={
                "placeholder": "Ej: 500mg",
                "id": "id_concentracion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "via_administracion": forms.Select(attrs={
                "id": "id_via_administracion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "cantidad": forms.NumberInput(attrs={
                "min": 0,
                "id": "id_cantidad",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "precio": forms.NumberInput(attrs={
                "min": 0,
                "step": "0.01",
                "id": "id_precio",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-300 focus:ring-blue-500 focus:border-blue-500",
            }),
            "comercial": forms.CheckboxInput(attrs={
                "class": "form-check-input rounded text-blue-600 focus:ring-blue-500 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800",
            }),
            "foto": forms.ClearableFileInput(attrs={
                "class": "block w-full text-sm text-gray-900 border border-gray-300 rounded-lg cursor-pointer bg-gray-50 dark:text-gray-400 dark:bg-principal dark:border-gray-600 focus:outline-none",
            }),
            "activo": forms.CheckboxInput(attrs={
                "class": "form-check-input rounded text-blue-600 focus:ring-blue-500 dark:ring-offset-gray-800 dark:focus:ring-offset-gray-800",
            }),
        }
    def clean_name(self):
        name = self.cleaned_data.get("nombre")
        return name.upper()
    
    # def clean_icon(self):
    #     icon = self.cleaned_data['descripcion']
    #     if not icon:
    #         raise forms.ValidationError("El campo descripcion es requerido.")
        
    #     # Patrones para FontAwesome v5 y v6
    #     patterns = [
    #         r'^(fas|far|fal|fad|fab|fa)\s+fa-\w+',      # fas fa-user (v5)
    #         r'^fa-(solid|regular|light|duotone|brands)\s+fa-\w+',  # fa-solid fa-user (v6)
    #         r'^fa-\w+$',                                 # fa-user (formato simple)
    #     ]
        
    #     is_valid = any(re.match(pattern, icon) for pattern in patterns)
        
    #     if not is_valid:
    #         raise forms.ValidationError(
    #             "Formato de ícono inválido. Ejemplos válidos: "
    #             "'fas fa-user', 'fa-solid fa-person', 'fa-home'"
    #         )
        
    #     return icon