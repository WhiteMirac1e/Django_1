from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.DecimalField(max_digits=8, decimal_places=2)
    adress = models.CharField(max_length=100)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, number: {self.number}, adress: {self.adress}, date_add: {self.date_add}'
    
    
class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    count = models.DecimalField(max_digits=8, decimal_places=2)
    date_add = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Product name: {self.name}, price: {self.price},  count: {self.count}, date_add: {self.date_add}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)
    date_ordered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Customer: {self.customer.name}, products: {self.products},  date_ordered: {self.date_ordered}, total_price: {self.total_price}'