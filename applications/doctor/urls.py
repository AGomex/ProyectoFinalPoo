from django.urls import path

from applications.doctor.views.atencion_medica import AtencionListView, AtencionCreateView, AtencionUpdateView, \
    AtencionDeleteView
from applications.doctor.views.servicioadicional import ServicioAdicionalesListView, ServicioAdicionalesCreateView, ServicioAdicionalesUpdateView, ServicioAdicionalesDeleteView
from applications.doctor.views.horarioatencion import HorarioAtencionListView, HorarioAtencionCreateView, \
    HorarioAtencionUpdateView, HorarioAtencionDeleteView

app_name='doctor' # define un espacio de nombre para la aplicacion
urlpatterns = [
    # Rutas  para vistas relacionadas con Doctor
    path('atencion_list/', AtencionListView.as_view(), name="atencion_list"),
    path('atencion_create/', AtencionCreateView.as_view(), name="atencion_create"),
    path('atencion_update/<int:pk>/', AtencionUpdateView.as_view(), name="atencion_update"),
    path('atencion_delete/<int:pk>/', AtencionDeleteView.as_view(), name="atencion_delete"),

    # Rutas para Servicio Adicionales
    path('serviciosadicionales_list/', ServicioAdicionalesListView.as_view(), name="serviciosadicionales_list"),
    path('serviciosadicionales_create/', ServicioAdicionalesCreateView.as_view(), name="serviciosadicionales_create"),
    path('serviciosadicionales_update/<int:pk>/', ServicioAdicionalesUpdateView.as_view(), name="serviciosadicionales_update"),
    path('serviciosadicionales_delete/<int:pk>/', ServicioAdicionalesDeleteView.as_view(), name="serviciosadicionales_delete"),

    # Rutas para Horario de Atencion
    path('horarioatenciones_list/', HorarioAtencionListView.as_view(), name="horarioatenciones_list"),
    path('horarioatenciones_create/', HorarioAtencionCreateView.as_view(), name="horarioatenciones_create"),
    path('horarioatenciones_update/<int:pk>/', HorarioAtencionUpdateView.as_view(), name="horarioatenciones_update"),
    path('horarioatenciones_delete/<int:pk>/', HorarioAtencionDeleteView.as_view(), name="horarioatenciones_delete"),

]