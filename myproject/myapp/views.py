from django.http import HttpResponse
from .models import FoodOrder

def order_list(request):
    orders = FoodOrder.objects.all()
    output = ""
    for order in orders:
        output += f"{order.customer_name} - {order.food_item} - Qty: {order.quantity} - ₹{order.price} - Delivered: {order.is_delivered}<br>"
    return HttpResponse(output)
    