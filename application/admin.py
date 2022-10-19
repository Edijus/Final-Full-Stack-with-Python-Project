from django.contrib import admin
from .models import User, Service, OrderDetail, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Service)
admin.site.register(OrderDetail)
admin.site.register(Order)
