from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import render
from applications.core.models import Medicamento
from django.db.models import Avg 

@csrf_exempt
def chatbot_view(request):
    if request.method == 'POST':
        question = request.POST.get('message', '').lower()  # ← Aquí usamos POST.get

        if 'cuántos' in question and 'medicamento' in question and 'activo' in question:
            count = Medicamento.objects.filter(activo=True).count()
            return JsonResponse({'response': f"Hay {count} medicamentos activos."})

        elif 'cuántos' in question and 'medicamento' in question:
            count = Medicamento.objects.count()
            return JsonResponse({'response': f"Hay un total de {count} medicamentos en el sistema."})

        elif 'orales' in question or 'oral' in question:
            count = Medicamento.objects.filter(via_administracion__icontains='oral').count()
            return JsonResponse({'response': f"Hay {count} medicamentos con vía oral."})

        elif 'precio' in question:
            avg = Medicamento.objects.aggregate(promedio=Avg('precio'))['promedio']

            return JsonResponse({'response': f"El precio promedio de los medicamentos es ${avg:.2f}."})

        elif 'sin stock' in question or 'agotado' in question:
            count = Medicamento.objects.filter(cantidad=0).count()
            return JsonResponse({'response': f"Hay {count} medicamentos sin stock."})

        else:
            return JsonResponse({'response': "Lo siento, no entendí tu pregunta. Puedes preguntar por medicamentos activos, por vía, sin stock o total."})

    return render(request, 'base.html',)