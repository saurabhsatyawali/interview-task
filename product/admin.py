from django.contrib import admin
from product.models import productMainModel,productImageModel,productColourModel
# Register your models here.
admin.site.register(productMainModel)
admin.site.register(productColourModel)
admin.site.register(productImageModel)