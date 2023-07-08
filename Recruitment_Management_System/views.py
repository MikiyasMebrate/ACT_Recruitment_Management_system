from django.shortcuts import render
from Company.models import Social_Media 

social_medias = Social_Media.objects.all()
# Create your views here.
def index(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/index.html', context)

def job_list(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/job-list.html', context)

def job_detail(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/job-details.html', context)

def profile(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/user/profile.html', context)

def reset_password(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/reset-password.html', context)

def login(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/sign-in.html', context)

def sign_up(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/sign-up.html', context)

def user_dashboard(request):
    return render(request, 'RMS/user/candidate-dashboard.html')

def user_resume(request):
    return render(request, 'RMS/user/dashboard-add-resume.html')

def user_applied_jobs(request):
    return render(request, 'RMS/user/dashboard-applied-jobs.html')

def user_bookmark(request):
    return render(request, 'RMS/user/dashboard-saved-jobs.html')

def user_change_password(request):
    return render(request, 'RMS/user/dashboard-change-password.html')

def user_profile(request):
    return render(request, 'RMS/user/dashboard-my-profile.html')