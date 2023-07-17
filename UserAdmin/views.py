from django.shortcuts import render

# Create your views here.
def admin_index(request):
    return render(request, 'admin-user/Dashboard.html')

def customer_view(request):
    return render(request, 'admin-user/Customers-List.html')

def customer_detail_view(request):
    return render(request, 'admin-user/Customers-Detail.html')

def discount(request):
    return render(request, 'admin-user/discount.html')

def Orders_detail(request):
    return render(request, 'admin-user/Orders-Detail.html')

def order_list(request):
    return render(request, 'admin-user/Orders-List.html')

def general_setting(request):
    return render(request, 'admin-user/Settings-General.html')

def product_detail(request):
    return render(request, 'admin-user/Products-Detail.html')

def product_list(request):
    return render(request, 'admin-user/Products-List.html')

def settings(request):
    return render(request, 'admin-user/Settings.html')

def Shipping(request):
    return render(request, 'admin-user/Shipping.html')

def Storefront_cart(request):
    return render(request, 'admin-user/Storefront-Cart.html')

def Storefront_Categories(request):
    return render(request, 'admin-user/Storefront-Categories.html')

def Storefront_Checkout(request):
    return render(request, 'admin-user/Storefront-Checkout.html')

def Storefront_Detail(request):
    return render(request, 'admin-user/Storefront-Detail.html')

def Storefront_Filters(request):
    return render(request, 'admin-user/Storefront-Filters.html')

def Storefront_Home(request):
    return render(request, 'admin-user/Storefront-Home.html')

