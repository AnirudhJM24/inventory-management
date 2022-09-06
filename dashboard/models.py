from django.db import models
from django.contrib.auth.models import User
# Create your models here.
CATEGORY = (
    ('Stationary', 'Stationary'),
     ('Electronics', 'Electronics'),
      ('Essentials', 'Essentials'), 
)

class Product(models.Model):

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=CATEGORY)
    quantity = models.PositiveIntegerField()


    def __str__(self):
        return f'{self.name}'

class Order(models.Model):

    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    staff = models.ForeignKey(User,models.CASCADE)
    order_quantity = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return f'{self.product} - {self.order_quantity}'


