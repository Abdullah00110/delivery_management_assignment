from django.contrib import admin
from .models import DeliveryPerson, Order, DeliveryAssignment

@admin.register(DeliveryPerson)
class DeliveryPersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone_number', 'is_available']
    list_filter = ['is_available']
    search_fields = ['name', 'phone_number']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'pickup_location', 'delivery_location', 'order_status', 'assigned_to']
    list_filter = ['order_status']
    search_fields = ['pickup_location', 'delivery_location']

@admin.register(DeliveryAssignment)
class DeliveryAssignmentAdmin(admin.ModelAdmin):
    list_display = ['order', 'delivery_person', 'assigned_at']
    list_filter = ['assigned_at']
