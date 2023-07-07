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

def bookmark_job(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/bookmark-jobs.html', context) 

def profile(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/profile.html', context)

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

def error(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/404-error.html', context)