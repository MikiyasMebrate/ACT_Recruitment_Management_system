from django.shortcuts import render
from Company.models import Social_Media 
from .forms import CandidateForm
from .models import Skill
from django.contrib import messages
import csv
from django.core.management.base import BaseCommand



social_medias = Social_Media.objects.all()
# Create your views here.
def csv_file_reader():
    with open('skill_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            for j in i:
                    Skill.objects.create(title = j)
    
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
    skills = Skill.objects.all()
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            form.save()
            messages.success(request, 'Your Resume has been successfully Created!')
            form = CandidateForm()
    else:
        form = CandidateForm()
        
    context = {
        'form' : form,
        'skills' : skills
        }
    return render(request, 'RMS/user/dashboard-add-resume.html', context)

def user_applied_jobs(request):
    return render(request, 'RMS/user/dashboard-applied-jobs.html')

def user_bookmark(request):
    return render(request, 'RMS/user/dashboard-saved-jobs.html')

def user_change_password(request):
    return render(request, 'RMS/user/dashboard-change-password.html')

def user_profile(request):
    return render(request, 'RMS/user/dashboard-my-profile.html')