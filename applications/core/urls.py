from django.urls import path
from applications.core.views.pacientefind import paciente_find
from applications.core.views.tiposangre import TipoSangreCreateView, TipoSangreDeleteView, TipoSangreListView, TipoSangreUpdateView
from applications.core.views.paciente import PacienteCreateView, PacienteDeleteView, PacienteListView, PacienteUpdateView
from applications.core.views.tipogasto import TipoGastoCreateView, TipoGastoDeleteView, TipoGastoListView, TipoGastoUpdateView
from applications.core.views.gastomensual import GastoMensualCreateView, GastoMensualDeleteView, GastoMensualListView, GastoMensualUpdateView  
from applications.core.views.doctor import (
    DoctorListView, DoctorCreateView, DoctorUpdateView, DoctorDeleteView
) 
from applications.core.views.especialidad import (
    EspecialidadListView, EspecialidadCreateView,
    EspecialidadUpdateView, EspecialidadDeleteView
)
from applications.core.views.empleado import (
    EmpleadoListView, EmpleadoCreateView, EmpleadoUpdateView, EmpleadoDeleteView
)
from applications.core.views.cargo import (
    CargoListView, CargoCreateView, CargoUpdateView, CargoDeleteView
)
from applications.core.views.tipomedicamento import TipoMedicamentoCreateView, TipoMedicamentoDeleteView, TipoMedicamentoListView, TipoMedicamentoUpdateView
from applications.core.views.marcamedicamento import MarcamedicamentoCreateView, MarcamedicamentoDeleteView, MarcamedicamentoListView, MarcamedicamentoUpdateView
from applications.core.views.medicamento import MedicamentoCreateView, MedicamentoDeleteView, MedicamentoListView, MedicamentoUpdateView
from applications.core.views.diagnostico import DiagnosticoCreateView,DiagnosticoListView,DiagnosticoUpdateView,DiagnosticoDeleteView

app_name='core' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Pacientes
    path('paciente_find/', paciente_find, name="paciente_find"),

    # rutas de tiposangres
    path('tiposangre_list/',TipoSangreListView.as_view() ,name="tiposangre_list"),
    path('tiposangre_create/', TipoSangreCreateView.as_view(),name="tiposangre_create"),
    path('tiposangre_update/<int:pk>/', TipoSangreUpdateView.as_view(),name='tiposangre_update'),
    path('tiposangre_delete/<int:pk>/', TipoSangreDeleteView.as_view(),name='tiposangre_delete'),

    # rutas para tipogastos
    path('tipogasto_list/', TipoGastoListView.as_view(), name='tipogasto_list'),
    path('tipogasto_create/', TipoGastoCreateView.as_view(), name='tipogasto_create'),
    path('tipogasto_update/<int:pk>/', TipoGastoUpdateView.as_view(), name='tipogasto_update'),
    path('tipogasto_delete/<int:pk>/', TipoGastoDeleteView.as_view(), name='tipogasto_delete'),

    # rutas para gastos mensuales
    path('gastomensual_list/', GastoMensualListView.as_view(), name='gastomensual_list'),
    path('gastomensual_create/', GastoMensualCreateView.as_view(), name='gastomensual_create'),
    path('gastomensual_update/<int:pk>/', GastoMensualUpdateView.as_view(), name='gastomensual_update'),
    path('gastomensual_delete/<int:pk>/', GastoMensualDeleteView.as_view(), name='gastomensual_delete'),

    # rutas para pacientes
    path('paciente_list/', PacienteListView.as_view(), name='paciente_list'),
    path('paciente_create/', PacienteCreateView.as_view(), name='paciente_create'),
    path('paciente_update/<int:pk>/', PacienteUpdateView.as_view(), name='paciente_update'),
    path('paciente_delete/<int:pk>/', PacienteDeleteView.as_view(), name='paciente_delete'),

    path('doctor_list/', DoctorListView.as_view(), name="doctor_list"),
    path('doctor_create/', DoctorCreateView.as_view(), name="doctor_create"),
    path('doctor_update/<int:pk>/', DoctorUpdateView.as_view(), name='doctor_update'),
    path('doctor_delete/<int:pk>/', DoctorDeleteView.as_view(), name='doctor_delete'),

    # Rutas para Especialidades Médicas
    path('especialidad_list/', EspecialidadListView.as_view(), name="especialidad_list"),
    path('especialidad_create/', EspecialidadCreateView.as_view(), name="especialidad_create"),
    path('especialidad_update/<int:pk>/', EspecialidadUpdateView.as_view(), name='especialidad_update'),
    path('especialidad_delete/<int:pk>/', EspecialidadDeleteView.as_view(), name='especialidad_delete'),

    # Rutas para Empleados
    path('empleado_list/', EmpleadoListView.as_view(), name="empleado_list"),
    path('empleado_create/', EmpleadoCreateView.as_view(), name="empleado_create"),
    path('empleado_update/<int:pk>/', EmpleadoUpdateView.as_view(), name='empleado_update'),
    path('empleado_delete/<int:pk>/', EmpleadoDeleteView.as_view(), name='empleado_delete'),    

    # Rutas para Cargos
    path('cargo_list/', CargoListView.as_view(), name="cargo_list"),
    path('cargo_create/', CargoCreateView.as_view(), name="cargo_create"),
    path('cargo_update/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargo_delete/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),

#tipo medicamento
    path('tipomedicamento_list/', TipoMedicamentoListView.as_view(), name='tipomedicamento_list'),
    path('tipomedicamento_create/', TipoMedicamentoCreateView.as_view(), name='tipomedicamento_create'),
    path('tipomedicamento_update/<int:pk>/', TipoMedicamentoUpdateView.as_view(), name='tipomedicamento_update'),
    path('tipomedicamento_delete/<int:pk>/', TipoMedicamentoDeleteView.as_view(), name='tipomedicamento_delete'),

 #Marca medicamento
    path('marcamedicamento_list/', MarcamedicamentoListView.as_view(), name='marcamedicamento_list'),
    path('marcamedicamento_create/', MarcamedicamentoCreateView.as_view(), name='marcamedicamento_create'),
    path('marcamedicamento_update/<int:pk>/', MarcamedicamentoUpdateView.as_view(), name='marcamedicamento_update'),
    path('marcamedicamento_delete/<int:pk>/', MarcamedicamentoDeleteView.as_view(), name='marcamedicamento_delete'),

  # Medicamento
    path('medicamento_list/', MedicamentoListView.as_view(), name='medicamento_list'),
    path('medicamento_create/', MedicamentoCreateView.as_view(), name='medicamento_create'),
    path('medicamento_update/<int:pk>/', MedicamentoUpdateView.as_view(), name='medicamento_update'),
    path('medicamento_delete/<int:pk>/', MedicamentoDeleteView.as_view(), name='medicamento_delete'),   

    #Diagnostico
    path('diagnostico_list/', DiagnosticoListView.as_view(), name='diagnostico_list'),
    path('diagnostico_create/', DiagnosticoCreateView.as_view(), name='diagnostico_create'),
    path('diagnostico_update/<int:pk>/', DiagnosticoUpdateView.as_view(), name='diagnostico_update'),
    path('diagnostico_delete/<int:pk>/', DiagnosticoDeleteView.as_view(), name='diagnostico_delete'),

]