from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'RMS/index.html')

def job_list(request):
    return render(request, 'RMS/job-list.html')

def job_detail(request):
    return render(request, 'RMS/job-details.html')

def bookmark_job(request):
    return render(request, 'RMS/bookmark-jobs.html') 

def profile(request):
    return render(request, 'RMS/profile.html')

def reset_password(request):
    return render(request, 'RMS/reset-password.html')

def login(request):
    return render(request, 'RMS/sign-in.html')

def sign_up(request):
    return render(request, 'RMS/sign-up.html')

def error(request):
    return render(request, 'RMS/404-error.html')