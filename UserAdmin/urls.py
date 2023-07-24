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
    path('applicant/', views.applicant_all, name='applicant'),
    path('applicant/<slug:slug>/', views.applicant_category, name='applicant_category'),
    path('applicant/<slug:slug>/<slug:slug2>/', views.applicant_detail, name='applicant_detail'),
    path('admin-list/', views.admin_account_list, name='admin-account-list'),
    path('admin-blog-list/', views.blog_lists, name='admin-blog-list'),
    path('admin-blog-detail/<slug:slug>', views.blog_detail, name='admin-blog-detail'),
]
