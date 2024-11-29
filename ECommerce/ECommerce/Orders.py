from django.db import models

class Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=100, 
                                    choices = [
                                        ('PENDING', 'Pending'),
                                        ('SHIPPED', 'Shipped'),
                                        ('DELIVERED', 'Delivered'),
                                        ('CANCELLED', 'Cancelled')
                                    ],
                                    default='PENDING')
    total_price = models.DecimalField(max_digits=10)

    def __str__(self):
        return f"Order {self.id} by {self.customer}"