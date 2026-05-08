from celery import shared_task
import random
from .models import Order


@shared_task
def process_payment(order_id, payment_number):
    order = Order.objects.get(id=order_id)

    # Валидация: чётный и не заканчивается на 0
    payment_number = int(payment_number)
    if payment_number % 2 == 0 and payment_number % 10 != 0:
        order.status = 'paid'
    else:
        order.status = 'error'
        order.payment_error = 'Ошибка оплаты: номер карты не прошёл проверку.'

    order.save()
    return f"Order {order_id} processed"