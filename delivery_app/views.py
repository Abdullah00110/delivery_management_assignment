from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import DeliveryPerson, Order, DeliveryAssignment
import json

@csrf_exempt
def assign_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            order_id = data.get('order_id')

            order = Order.objects.get(id=order_id)

            if order.assigned_to:
                return JsonResponse({'error': 'Order already assigned.'}, status=400)

            delivery_person = DeliveryPerson.objects.filter(is_available=True).first()

            if not delivery_person:
                return JsonResponse({'error': 'No available delivery person.'}, status=404)

            order.assigned_to = delivery_person
            order.save()

            delivery_person.is_available = False
            delivery_person.save()

            DeliveryAssignment.objects.create(
                delivery_person=delivery_person,
                order=order
            )

            return JsonResponse({
                'message': f"Order #{order.id} assigned to {delivery_person.name}"
            })

        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST method allowed.'}, status=405)


def list_assignments(request):
    if request.method == 'GET':
        assignments = DeliveryAssignment.objects.select_related('delivery_person', 'order')
        data = []

        for a in assignments:
            data.append({
                'order_id': a.order.id,
                'delivery_person': a.delivery_person.name,
                'pickup_location': a.order.pickup_location,
                'delivery_location': a.order.delivery_location,
                'assigned_at': a.assigned_at.strftime('%Y-%m-%d %H:%M:%S')
            })

        return JsonResponse(data, safe=False)

    return JsonResponse({'error': 'Only GET method allowed.'}, status=405)
