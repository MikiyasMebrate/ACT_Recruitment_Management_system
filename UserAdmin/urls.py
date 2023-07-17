from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_index, name='admin-dashboard'),
    path('candidate/', views.candidate_view, name='candidate'),
    path('candidate-detail/<str:id>/', views.candidate_detail_view, name='candidate-detail'),
    path('discount/', views.discount, name='discount'),
    path('order-detail/', views.Orders_detail, name='order-detail'),
    path('Orders-List/', views.order_list, name='order-list'),
    path('general-setting/', views.general_setting, name='general-setting'),
    path('product-detail/', views.product_detail, name='product-detail'),
    path('product-list/', views.product_list, name='product-list'),
    path('settings/', views.settings, name='setting'),
    path('Shipping/', views.Shipping, name='Shipping'),
    path('Storefront-Cart/', views.Storefront_cart, name='Storefront-Cart'),
    path('Storefront-Categories/', views.Storefront_Categories, name='Storefront-Categories'),
    path('Storefront-Checkout/', views.Storefront_Checkout, name='Storefront-Checkout'),
    path('Storefront_Detail/', views.Storefront_Detail, name='Storefront_Detail'),
    path('Storefront_Filters/', views.Storefront_Filters, name='Storefront_Filters'),
    path('Storefront-Home/', views.Storefront_Home, name='Storefront-Home.html')
]
