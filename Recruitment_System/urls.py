from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.registration_view, name="signup"),
    path('job-list/', views.job_list, name='job-list'),
    path('job-detail/<str:pk>', views.job_detail, name='Job-detail'),
    path('user-add-bookmark/<str:pk>', views.user_add_bookmark, name="user-add-bookmark"),
    path('user-remove-bookmark/<str:pk>', views.user_delete_bookmark, name='user-delete-bookmark'),
    path('user-apply-job/<str:pk>', views.user_apply_job, name='user-apply-job'),
    path('user-cancel-job/<str:pk>', views.user_cancel_job, name='user-cancel-job'),
    path('resetpassword/', views.reset_password, name='reset-password'),
    path('login/', views.login, name='login'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('user-add-resume/', views.user_resume, name='user-resume'),
    path('user-add-education/', views.user_add_education, name='user-add-education'),
    path('user-education/<str:pk>/',views.detail_user_education, name='detail-user-education'),
    path('user-delete-education/<str:pk>',views.user_delete_education, name='user-delete-education'),
    path('user-add-experience/', views.user_add_experience, name='user-add-experience'),
    path('user-experience/<str:pk>/',views.detail_user_experience, name='detail-user-experience'),
    path('user-delete-experience/<str:pk>',views.user_delete_experience, name='user-delete-experience'),
    path('user-applied-job/', views.user_applied_jobs, name='user-applied-job'),
    path('user-bookmark/', views.user_bookmark, name='user-bookmark'),
    path('user-change-password/', views.user_change_password, name='user-change-password')
]
