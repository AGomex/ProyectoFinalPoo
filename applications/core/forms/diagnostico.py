import re
from django import forms
from django.forms import ModelForm

from applications.core.models import Diagnostico

class DiagnosticoForm(ModelForm):
    class Meta:
        model = Diagnostico
        fields = [
            "codigo",
            "descripcion", 
            "datos_adicionales",
            "activo",          
        ]
        error_messages = {
          
            "codigo": {
                "unique": "Ya existe un codigo de tipo de medicamento con este codigo.",
            },
        }
        widgets = {
            "codigo": forms.TextInput(attrs={
                "placeholder": "Ingrese el Diagnostico",
                "id": "id_tipo",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
          
            "descripcion": forms.Textarea(attrs={
                "placeholder": "Desripcion del diagnostico",
                "id": "id_descripcion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "datos_adicionales": forms.TextInput(attrs={
                "placeholder": "Datos adicionales del diagnostico",
                "id": "id_descripcion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "activo": forms.CheckboxInput(attrs={
                "id": "id_activo",
                "class": "form-check-input",
            }),
        }
        labels = {
            "codigo": "Codigo del diagnostico",
            "descripcion": "Descripcion", 
            "datos_adicionales" : "Datos adicionales",  
            "activo" : "Activo",        
        }

    def clean_name(self):
        name = self.cleaned_data.get("codigo")
        return name.upper()