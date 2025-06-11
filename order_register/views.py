from django.shortcuts import render
from .forms import OrderForm

# Create your views here.

def order_list(request):
    return render(request, 'order_register/order_list.html')

def order_form(request):
    form = OrderForm()
    return render(request, "order_register/order_form.html",{'form':form})

def order_delete(request):
    return 

