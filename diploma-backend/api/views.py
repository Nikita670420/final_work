from rest_framework import viewsets
from apps.catalog.models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer

    # Фильтрация по названию и категории (как в ТЗ)
    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('search')
        if name:
            qs = qs.filter(name__icontains=name)
        return qs