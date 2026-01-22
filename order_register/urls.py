from django.urls import path,include
from . import views


urlpatterns = [

    path('home/', views.home, name='home'), #get request to render home page
    path('orders/', views.order_form, name='order_insert'), #get and post request for insert operaton
    path('<int:order_id>/', views.order_form,name='order_update'),#get and post req. for update operation
    path('delete/<int:order_id>/',views.order_delete, name='order_delete'),
    path('orders/lists/', views.order_list, name='order_list'),#get request to retrieve and display all orders 
    path('orders/showcase/', views.showcase, name= 'showcase'),#get a orders dummy page
   
    

]