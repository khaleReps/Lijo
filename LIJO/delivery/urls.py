from django.urls import path
from .views import (
    CustomerListView, CustomerDetailView,
    RestaurantListView, RestaurantDetailView,
    MenuListView, MenuDetailView,
    OrderCreateView, OrderSuccessView,
)

app_name = 'delivery'
urlpatterns = [
    path('customers/', CustomerListView.as_view(), name='customer_list'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer_detail'),
    path('restaurants/', RestaurantListView.as_view(), name='restaurant_list'),
    path('restaurants/<int:pk>/', RestaurantDetailView.as_view(), name='restaurant_detail'),
    path('menus/', MenuListView.as_view(), name='menu_list'),
    path('menus/<int:pk>/', MenuDetailView.as_view(), name='menu_detail'),
    path('order/create/', OrderCreateView.as_view(), name='order_create'),
    path('order/success/<int:pk>/', OrderSuccessView.as_view(), name='order_success'),
]
