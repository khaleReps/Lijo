from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Customer, Restaurant, Menu, Order, OrderItem

class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'

class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customer_detail.html'
    context_object_name = 'customer'

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'
    context_object_name = 'restaurants'

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'
    context_object_name = 'restaurant'

class MenuListView(ListView):
    model = Menu
    template_name = 'menu_list.html'
    context_object_name = 'menus'

class MenuDetailView(DetailView):
    model = Menu
    template_name = 'menu_detail.html'
    context_object_name = 'menu'

class OrderCreateView(CreateView):
    model = Order
    template_name = 'order_create.html'
    fields = ['customer', 'restaurant', 'order_date', 'total_amount']
    success_url = '/order/success/'

class OrderSuccessView(DetailView):
    model = Order
    template_name = 'order_success.html'
    context_object_name = 'order'
