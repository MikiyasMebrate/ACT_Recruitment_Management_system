from django.urls import path
from . import views

urlpatterns = [
    path('', views.admin_index, name='admin-dashboard'),
    path('candidate/', views.candidate_view, name='candidate'),
    path('candidate-detail/<slug:slug>/', views.candidate_detail_view, name='candidate-detail'),
    path('job-list-admin/', views.job_board_view, name='job-list-admin'),
    path('job-detail-admin/<slug:slug>', views.job_detail_view, name='job-detail-admin'),
    path('job-delete-admin/<slug:slug>', views.job_delete_view, name='delete-job-admin'),
    path('department-admin/', views.department, name='department-admin'),
    path('department-detail-admin/<slug:slug>', views.department_detail, name='department-detail-admin'),
    path('department-delete-admin/<slug:slug>', views.department_delete, name='delete-department-admin'),
    
    path('discount/', views.discount, name='discount'),
    path('general-setting/', views.general_setting, name='general-setting'),
    path('settings/', views.settings, name='setting'),
    path('Shipping/', views.Shipping, name='Shipping'),
    path('Storefront-Cart/', views.Storefront_cart, name='Storefront-Cart'),
    path('Storefront-Categories/', views.Storefront_Categories, name='Storefront-Categories'),
    path('Storefront-Checkout/', views.Storefront_Checkout, name='Storefront-Checkout'),
    path('Storefront_Detail/', views.Storefront_Detail, name='Storefront_Detail'),
    path('Storefront_Filters/', views.Storefront_Filters, name='Storefront_Filters'),
    path('Storefront-Home/', views.Storefront_Home, name='Storefront-Home.html')
]
