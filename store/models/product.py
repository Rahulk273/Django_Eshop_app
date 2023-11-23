from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='', null=True,
                                   blank=True)  # if we do not pass description then the default value is null or either empty string
    image = models.ImageField(upload_to='uploads/products/')

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in = ids)


    # method for collecting product
    # static method
    @staticmethod  # annotation / decorator
    def get_all_products():
        return Product.objects.all()  # go to views.py and collect data in views.py we have to import product

    #filter or retrieving data from database or we say we want category wise
    #product
    @staticmethod  # annotation / decorator
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
