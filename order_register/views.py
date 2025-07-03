from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from .models import Order



def home(request):
    return render(request, 'order_register/home.html',{'title': 'Home'})


def order_list(request):
    orders = Order.objects.all()
    return render(request, 'order_register/order_list.html', {'order_list': orders})


def order_form(request, order_id=0):
    context = {'form': Order()}
    if request.method == "GET":
        if order_id == 0:
            form = OrderForm()
        else:
            order = get_object_or_404(Order, pk=order_id)
            form = OrderForm(instance=order)
        return render(request, "order_register/order_form.html", {'form': form})
    
    else:  # POST request
        if order_id == 0:
            form = OrderForm(request.POST)
        else:
            order = get_object_or_404(Order, pk=order_id)
            form = OrderForm(request.POST, instance=order)

        if form.is_valid():
            form.save()
            messages.success(request, 'Order saved successfully!')
            return redirect('order_list')
        else:
            messages.error(request, 'Please correct the errors below.')
        
        return render(request, "order_register/order_form.html", {'form': form})


def order_delete(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    order.delete()
    messages.success(request, 'Order deleted successfully!')
    return redirect('order_list')