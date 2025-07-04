from django import forms
from django.forms import ModelForm
from applications.doctor.models import DetallePago

class DetallePagoForm(ModelForm):
    class Meta:
        model = DetallePago
        fields = [
            "servicio_adicional",
            "cantidad",
            "precio_unitario",
            "descuento_porcentaje",
            "aplica_seguro",
            "valor_seguro",
            "descripcion_seguro",
        ]
        widgets = {
            "servicio_adicional": forms.Select(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "cantidad": forms.NumberInput(attrs={
                "min": "1",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "precio_unitario": forms.NumberInput(attrs={
                "step": "0.01",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "descuento_porcentaje": forms.NumberInput(attrs={
                "min": "0",
                "max": "100",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "aplica_seguro": forms.CheckboxInput(attrs={
                "class": "form-check-input",
            }),
            "valor_seguro": forms.NumberInput(attrs={
                "step": "0.01",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
            "descripcion_seguro": forms.TextInput(attrs={
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
            }),
        }
        labels = {
            "servicio_adicional": "Servicio Adicional",
            "cantidad": "Cantidad",
            "precio_unitario": "Precio Unitario",
            "descuento_porcentaje": "Descuento (%)",
            "aplica_seguro": "Aplica Seguro",
            "valor_seguro": "Valor Seguro",
            "descripcion_seguro": "Descripción del Seguro",
        }
