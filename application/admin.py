from django.contrib import admin
from .models import User, Categories  # , OrderDetail, Order

# Register your models here.
admin.site.register(User)
admin.site.register(Categories)
# admin.site.register(OrderDetail)
# admin.site.register(Order)
