from django.forms import inlineformset_factory
from applications.doctor.models import Pago, DetallePago
from applications.doctor.forms.detallepago import DetallePagoForm

DetallePagoFormSet = inlineformset_factory(
    Pago,
    DetallePago,
    form=DetallePagoForm,
    fields = [
            "servicio_adicional",
            "cantidad",
            "precio_unitario",
            "descuento_porcentaje",
            "aplica_seguro",
            "valor_seguro",
            "descripcion_seguro",
        ],
    extra=1,
    can_delete=False 
)
