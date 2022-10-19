from django.shortcuts import render
from .models import Order, OrderDetail
from django.core.paginator import Paginator


# Create your views here.

def index(request):
    return render(request, 'index.html')


def show_orders(request, page=1):
    orders_per_page = 1
    orders = Order.objects.order_by('-date_created').all()
    paginator = Paginator(orders, orders_per_page)
    paginated_orders = paginator.get_page(page)
    context = {
        'orders': paginated_orders
    }
    return render(request, 'show_orders.html', context=context)


def show_order(request, id):
    order_details = OrderDetail.objects.filter(order=id).all()
    context = {
        'order_details': order_details
    }
    return render(request, 'show_order.html', context=context)
