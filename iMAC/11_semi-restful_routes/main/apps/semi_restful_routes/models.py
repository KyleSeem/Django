from __future__ import unicode_literals

from django.db import models
import re

CURRENCY_REGEX = re.compile(r'^\d*\.\d{2}$')

# Create your models here.
class ProductManager(models.Manager):
    def create(self, postData):
        alerts = []

        if len(postData['name']) < 1:
            alerts.append('Product name cannot be left blank.')

        if len(postData['description']) < 1:
            alerts.append('Product description cannot be left blank.')

        if len(postData['price']) < 1:
            alerts.append('Product price cannot be left blank.')
        elif not CURRENCY_REGEX.match(postData['price']):
            print ('bad price format')
            alerts.append('Invalid currency format.')

        if alerts:
            print (alerts)
            return (False, alerts)
        else:
            print ('successful product creation')
            product = Product.objects.create(name=postData['name'])
            Description.objects.create(product=product, description=postData['description'])
            Price.objects.create(product=product, price=postData['price'])
            return (True, 'success')


    def change(self, postData, id):
        product = Product.objects.get(id=id)
        alerts = []

        if len(postData['name']) < 1:
            alerts.append('Product name cannt be left blank.')

        if len(postData['description']) < 1:
            alerts.append('Product description cannt be left blank.')

        if len(postData['price']) < 1:
            alerts.append('Product price cannt be left blank.')
        elif not CURRENCY_REGEX.match(postData['price']):
            alerts.append('Invalid currency format.')

        if alerts:
            return (False, alerts)
        else:
            Product.objects.filter(id=id).update(name=postData['name'])
            Description.objects.filter(product=product).update(description=postData['description'])
            Price.objects.filter(product=product).update(price=postData['price'])
            return(True, 'Product successfully updated.')


class Product(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    productManager = ProductManager()
    objects = models.Manager()


class Description(models.Model):
    description = models.TextField(max_length=500)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Price(models.Model):
    price = models.DecimalField(max_digits=7, decimal_places=2)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
