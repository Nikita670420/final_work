from django.db import models
from django.conf import settings
from apps.catalog.models import Product

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='created')
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    payment_error = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)