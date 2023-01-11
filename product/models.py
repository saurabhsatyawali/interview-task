from django.db import models

# Create your models here.
class productMainModel(models.Model):
    title=models.CharField(max_length=40)
    description=models.CharField(max_length=200)
    price=models.IntegerField()
    unique_code=models.CharField(max_length=5,unique=True)
    size=models.CharField(max_length=2,choices=(('10','10'),('20','20'),('30','30')))
    quality=models.CharField(max_length=10,choices=(('high','high'),('low','low'),('medium','medium')))


class productColourModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    color=models.CharField(max_length=10,choices=(('red','red'),('blue','blue'),('green','green'),('black','black')))

class productImageModel(models.Model):
    product=models.ForeignKey(productMainModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='product_images')
