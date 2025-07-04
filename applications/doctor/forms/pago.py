import re
from django import forms
from django.forms import ModelForm

from applications.doctor.models import Pago

class PagoForm(ModelForm):
    class Meta:
        model = Pago
        fields = [
            "atencion",
            "metodo_pago", 
            "monto_total", 
            "estado",
            "fecha_pago",
            "nombre_pagador",  
            "referencia_externa",
            "evidencia_pago",
            "observaciones",
            "activo",    
        ]
        error_messages = {
          
            "atencion": {
                "unique": "Ya existe una atencion con este nombre.",
            },
        }
        widgets = {
            "atencion": forms.Select(attrs={
                "id": "id_atencion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
          
            "metodo_pago": forms.Select(attrs={
                "id": "id_metodo_pago",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),

            "monto_total": forms.NumberInput(attrs={
                "id": "id_monto_total",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),

            "estado": forms.Select(attrs={
                "id": "id_estado",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),

            "fecha_pago": forms.DateInput(attrs={
                "id": "id_fecha_pago",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                "type": "date",
            }),

            "fecha_creacion": forms.DateInput(attrs={
                "id": "id_fecha_creacion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                "type": "date",
            }),

            "nombre_pagador": forms.TextInput(attrs={
                "id": "id_nombre_pagador",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),

            "referencia_externa": forms.TextInput(attrs={
                "id": "id_referencia_externa",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),

            "evidencia_pago": forms.ClearableFileInput(attrs={
                "id": "id_evidencia_pago",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }), 

            "observaciones": forms.Textarea(attrs={
                "id": "id_observaciones",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                "rows": 3,
            }),

            "activo": forms.CheckboxInput(attrs={
                "id": "id_activo",
                "class": "form-check-input",
            }),
        }
        labels = {
            "atencion": "Atención",
            "metodo_pago": "Método de Pago",
            "monto_total": "Monto Total",
            "estado": "Estado",
            "fecha_pago": "Fecha de Pago",
            "fecha_creacion": "Fecha de Creación",
            "nombre_pagador": "Nombre del Pagador",
            "referencia_externa": "Referencia Externa",
            "evidencia_pago": "Evidencia de Pago",
            "observaciones": "Observaciones",
            "activo": "Activo",         
        }

    def clean_name(self):
        name = self.cleaned_data.get("tipo")
        return name.upper()
    
    def clean_icon(self):
        icon = self.cleaned_data['descripcion']
        if not icon:
            raise forms.ValidationError("El campo descripcion es requerido.")
        
        # Patrones para FontAwesome v5 y v6
        patterns = [
            r'^(fas|far|fal|fad|fab|fa)\s+fa-\w+',      # fas fa-user (v5)
            r'^fa-(solid|regular|light|duotone|brands)\s+fa-\w+',  # fa-solid fa-user (v6)
            r'^fa-\w+$',                                 # fa-user (formato simple)
        ]
        
        is_valid = any(re.match(pattern, icon) for pattern in patterns)
        
        if not is_valid:
            raise forms.ValidationError(
                "Formato de ícono inválido. Ejemplos válidos: "
                "'fas fa-user', 'fa-solid fa-person', 'fa-home'"
            )
        
        return icon