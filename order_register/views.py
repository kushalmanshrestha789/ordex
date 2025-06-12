from django.shortcuts import render,redirect
from .forms import OrderForm

# Create your views here.

def order_list(request):
    return render(request, 'order_register/order_list.html')

def order_form(request):
     if request.method == "GET":
          form = OrderForm()
          return render(request, "order_register/order_form.html",{'form':form})
     else:
         form = OrderForm(request.POST)
         if form.is_valid():
          form.save()
          return redirect('/orders/lists/')
def order_delete(request):
    return 

