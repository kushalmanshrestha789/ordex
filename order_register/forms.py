from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        # fields = '__all__' # Adjust fields as necessary 
        fields = ( 'product_name','customer_name', 'quantity','order_status')
        labels = {
            'product_name': 'Product Name',
            'customer_name': 'Customer Name',
            'quantity': 'Quantity',
            'order_status': 'Order Status'}
        # In futue, you should change this option to the status of the product
    def __init__(self,*args, **kwargs):
           super(OrderForm,self).__init__(*args, **kwargs)
           self.fields['order_status'].empty_label = "Select Order Status"
           self.fields['quantity'].widget.attrs.update({'min': '1','max':'1000'})
        #    self.fields['quantity'].required = False # Adjust as necessary Use this if filling the quantity is not required
             