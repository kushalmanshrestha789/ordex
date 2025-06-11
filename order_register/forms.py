from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = '__all__' # Adjust fields as necessary 
        fields = ( 'product_name','customer_name', 'quantity')

