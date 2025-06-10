from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.order_form),
    path('list/',views.order_list),
]
