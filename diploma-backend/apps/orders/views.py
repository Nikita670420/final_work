from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Order
from .tasks import process_payment


class PaymentView(APIView):
    def post(self, request):
        order_id = request.data.get('order_id')
        payment_number = request.data.get('number')

        # Запуск задачи в Celery
        process_payment.delay(order_id, payment_number)

        return Response({"message": "Ждём подтверждения оплаты от платёжной системы"})