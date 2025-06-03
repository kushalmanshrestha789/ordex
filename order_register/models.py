from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name} - {self.product_name}"
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Customer {self.customer_id} - {self.name}"