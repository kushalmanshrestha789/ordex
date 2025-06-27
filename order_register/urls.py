from django.urls import path,include
from . import views

urlpatterns = [


    path('', views.order_form, name='order_insert'), #get and post request for insert operaton
    path('<int:order_id>/', views.order_form,name='order_update'),#get and post req. for update operation
    path('delete/<int:order_id>/',views.order_delete, name='order_delete'),
    path('orders/lists/', views.order_list, name='order_list')#get request to retrieve and display all orders
    

]