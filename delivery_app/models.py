from django.db import models

# Create your models here.
class DeliveryPerson(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    is_available = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
class Order(models.Model):
    pickup_location = models.CharField(max_length=255)
    delivery_location = models.CharField(max_length=255)
    order_status = models.CharField(
        max_length=20,
        choices=[('pending', 'Pending'), ('delivered', 'Delivered')],
        default='pending'
    )
    assigned_to = models.ForeignKey(DeliveryPerson, null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"Order #{self.id}"
class DeliveryAssignment(models.Model):
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.delivery_person.name} → Order #{self.order.id}"