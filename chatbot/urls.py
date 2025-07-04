from django.urls import path
from .views import chatbot_view  # si tu vista está en views.py del proyecto raíz

urlpatterns = [
    path('', chatbot_view, name='chatbot_view'),
]