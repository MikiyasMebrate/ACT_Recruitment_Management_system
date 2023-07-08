from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('job-list/', views.job_list, name='job-list'),
    path('job-detail/', views.job_detail, name='Job-detail'),
    path('profile/', views.profile, name='profile'),
    path('resetpassword/', views.reset_password, name='reset-password'),
    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('user-dashboard/', views.user_dashboard, name='user-dashboard'),
    path('user-profile/', views.user_profile, name='user-profile'),
    path('user-add-resume/', views.user_resume, name='user-resume'),
    path('user-applied-job/', views.user_applied_jobs, name='user-applied-job'),
    path('user-bookmark/', views.user_bookmark, name='user-bookmark'),
    path('user-change-password/', views.user_change_password, name='user-change-password')
]
