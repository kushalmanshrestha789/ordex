from django.shortcuts import render

# Create your views here.

def order_list(request):
    return render(request, 'order_register/order_list.html')

def order_form(request):
    return render(request, "order_register/order_form.html")

def order_delete(request):
    return 

