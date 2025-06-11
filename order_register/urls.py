from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.order_form),
    path('lists/',views.order_list),
]