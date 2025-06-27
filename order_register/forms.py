from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['customer_name', 'product_name', 'quantity', 'order_status']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Ensure crispy forms styling
        self.fields['customer_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter customer name'
        })
        
        self.fields['product_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Enter product name'
        })
        
        self.fields['quantity'].widget.attrs.update({
            'class': 'form-control',
            'min': '1'
        })
        
        # This is key - ensure the choice field has fresh choices
        self.fields['order_status'].widget.attrs.update({
            'class': 'form-select'
        })
        
        # Set labels
        self.fields['customer_name'].label = 'Customer Name'
        self.fields['product_name'].label = 'Product Name'
        self.fields['quantity'].label = 'Quantity'
        self.fields['order_status'].label = 'Order Status'