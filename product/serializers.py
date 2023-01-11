from rest_framework import serializers
from product.models import productMainModel

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fields=('title','description','price','unique_code','size','quality')