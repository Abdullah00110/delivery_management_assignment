from django.urls import path
from .views import assign_order, list_assignments

urlpatterns = [
    path('assign-order/', assign_order, name='assign_order'),
    path('assignments/', list_assignments, name='list_assignments'),
]
