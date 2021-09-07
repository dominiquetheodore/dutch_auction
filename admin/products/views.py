from products.serializers import ProductSerializer
from products.models import Product
from .producer import publish
from rest_framework import viewsets, status
from rest_framework.response import Response

class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #/api/products
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        publish()
        return Response(serializer.data)

    def create(self, request): #/api/products
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print('** product created in admin **')
        publish('product created', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def update(self, request, pk=None):
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data)
        serializer.is_valid(raise_exception=True)
        pass

    def destroy(self, request, pk=None):
        pass