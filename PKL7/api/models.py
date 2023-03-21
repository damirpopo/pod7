from django.db import models

class Prod(models.Model):
    produlct=models.CharField(max_length=5000,verbose_name='Товар')

    def __str__(self):
        return self.produlct


class Product(models.Model):
    name=models.ForeignKey(Prod,on_delete=models.CASCADE,verbose_name='Наименование')
    description=models.CharField(max_length=9999,verbose_name='Описание')
    pice=models.IntegerField(verbose_name='Цена')



class Cart(models.Model):
    producwt=models.ForeignKey(Prod,on_delete=models.CASCADE,verbose_name='Список товаров')



class Order(models.Model):
    prodct=models.ForeignKey(Prod,on_delete=models.CASCADE,verbose_name='Продукты')
    full_price=models.IntegerField(verbose_name='Общая стоимость заказа')







