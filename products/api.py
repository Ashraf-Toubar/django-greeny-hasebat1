#like view

from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product
from rest_framework.decorators import api_view


# @api_view(['GET'])
# def product_list_api(request):
#     products = Product.objects.all()[:10]
#     data = ProductSerializer(products, many = True).data
#     return Response({'Success':True, 'Product List': data})


# @api_view(['GET'])
# def product_detail(request, id):
#     product = Product.objects.get(id=id)
#     data = ProductSerializer(product).data
#     return Response({'Success':True, 'Product': data    })


from rest_framework import generics

# class ProdcutList(generics.ListAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

class ProdcutList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    
# class ProdcutDetail(generics.RetrieveAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

# class ProdcutDetail(generics.RetrieveUpdateAPIView):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()

class ProdcutDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()