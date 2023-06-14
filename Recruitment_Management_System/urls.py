from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('job-list/', views.job_list, name='job-list'),
    path('job-detail/', views.job_detail, name='Job-detail'),
    path('bookmark-job/', views.bookmark_job, name='bookmark-job'),
    path('profile/', views.profile, name='profile'),
    path('resetpassword/', views.reset_password, name='reset-password'),
    path('login/', views.login, name='login'),
    path('signup/', views.sign_up, name='signup'),
    path('404/', views.error, name='error')
]
