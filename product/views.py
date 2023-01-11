from django.shortcuts import render
from product.serializers import ProductSerializer
from product.models import productMainModel
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductListView(APIView):
    def get(self,request):
        # if pk is not None:
      
        products=productMainModel.objects.all()
        serialized_data=ProductSerializer(products,many=True)
        return Response(serialized_data.data)

class ProductDetailView(APIView):
    def get(self,request,pk):
            product=productMainModel.objects.get(pk=pk)
            print(product)
            serialized_data=ProductSerializer(product)
            return Response(serialized_data.data)


