from django.shortcuts import render, redirect
from Company.models import Social_Media, Contact
from .forms import CandidateForm, EducationForm, ExperienceForm
from .models import Skill, Candidate, Education, Experience, Job_Posting
from django.contrib import messages
import csv
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from Account.forms import CustomUserCreationForm, Login_Form
# Create your views here.

social_medias = []
def login_view(request):
    form = Login_Form(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email,password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('admin-dashboard')
        elif user is not None and user.is_candidate:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid Password or Email')
    context = {
        'form' : form
    }
    return render(request, 'RMS/sign-in.html', context)

def logout_view(request):
    logout(request)
    return render(request, 'RMS/sign-out.html')

def registration_view(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.is_candidate = True
            user.save()
            messages.success(request, 'Your Account has been Successfully Created! Please Login')
            return redirect('/login')    
    context = {
        'form' : form
    }

    return render(request, 'RMS/registrations.html', context)

def index(request):

    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/index.html', context)

def job_list(request):
    job = Job_Posting.objects.filter(job_status = True)
    context = {
        'social_medias' : social_medias,
        'job_list' : job
    }
    return render(request, 'RMS/job-list.html', context)

def job_detail(request, pk):
    job = Job_Posting.objects.get(pk=pk)
    company_info = Contact.objects.all().first()
    social_media = Social_Media.objects.all().first()
    context = {
        'social_medias' : social_medias,
        'job' : job,
        'company_info' : company_info,
        'social_media' : social_media
    }
    return render(request, 'RMS/job-details.html', context)

@login_required
def reset_password(request):
    context = {
        'social_medias' : social_medias,
    }
    return render(request, 'RMS/reset-password.html', context)

@login_required
def user_dashboard(request):
    return render(request, 'RMS/user/candidate-dashboard.html')

@login_required
def user_resume(request):
    skills = Skill.objects.all()
    try:
        user_per_info = Candidate.objects.get(user = request.user)
    except: 
        user_per_info = None
    print(user_per_info)
    form_personal_info = CandidateForm(request.POST or None, request.FILES or None, instance=user_per_info)

    if request.method == 'POST':
        if form_personal_info.is_valid():
            obj = form_personal_info.save(commit=False)
            obj.user = request.user
            obj.save()
            form_personal_info.save_m2m()
            messages.success(request, 'Your Resume has been successfully Created!')
            form_personal_info =  CandidateForm(request.POST or None, request.FILES or None, instance=user_per_info)
            return redirect('user-dashboard')
    context = {
        'form' : form_personal_info,
        'skills' : skills,
        'candidate' : user_per_info
        }
    return render(request, 'RMS/user/dashboard-add-personal-info.html', context)

@login_required
def user_add_education(request):
    education = Education.objects.filter(candidate = request.user)
    form_education = EducationForm(request.POST or None)
    if request.method == 'POST':
        if form_education.is_valid():
            obj = form_education.save(commit=False)
            obj.candidate = request.user
            obj.save()
            messages.success(request, 'Your Education Status has been successfully Updated!')
            form_education = EducationForm()

    context = {
        'form' : form_education,
        'user_education' : education
        }
    return render(request, 'RMS/user/dashboard-add-education.html', context)

@login_required
def user_delete_education(request, pk):
    education = Education.objects.get(pk = pk)

    if education.delete():
        messages.success(request, 'Successfully Deleted!')
        return redirect('user-add-education')
    else:
        messages.error(request,'Your request has not been Unsuccessful Please try again!')
        return redirect('user-add-education')
    
@login_required
def detail_user_education(request, pk):
    education =  Education.objects.get(pk = pk)
    form = EducationForm(request.POST or None, instance=education)
    education_list = Education.objects.filter(candidate = request.user).exclude(pk = pk)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.candidate = request.user
            obj.save()
            messages.success(request, 'Your Education Status has been successfully Updated!')
            redirect('user-add-education')
    context = {
        'form' : form,
        'education': education,
        'user_education':education_list,
    }
    return render(request, 'RMS/user/dashboard-education-detail.html', context)

@login_required
def user_add_experience(request):
    form_experience = ExperienceForm(request.POST or None)
    experience = Experience.objects.all()
    if request.method == 'POST':
        if form_experience.is_valid():
            obj = form_experience.save(commit=False)
            obj.candidate = request.user
            obj.save()
            messages.success(request, 'Your Experience Status has been successfully Updated!')
            form_experience = EducationForm()

    context = {
        'form' : form_experience,
        'user_experience' : experience
        }
    return render(request, 'RMS/user/dashboard-add-experience.html', context)

@login_required
def detail_user_experience(request, pk):
    experience = Experience.objects.get(pk = pk)
    form = ExperienceForm(request.POST or None, instance=experience)
    experience_list = Experience.objects.filter(candidate = request.user).exclude(pk = pk)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.candidate = request.user
            obj.save()
            messages.success(request, 'Your Experience Status has been successfully Updated!')
            redirect('user-add-experience')
    context = {
        'form' : form,
        'experience' : experience,
        'user_experience' : experience_list
    }

    return render(request,'RMS/user/dashboard-experience-detail.html', context)

@login_required
def user_delete_experience(request, pk):
    experience = Experience.objects.get(pk = pk)

    if experience.delete():
        messages.success(request, 'Successfully Deleted!')
        return redirect('user-add-experience')
    else:
        messages.error(request,'Your request has not been Unsuccessful Please try again!')
        return redirect('user-add-experience')

@login_required
def user_applied_jobs(request):
    return render(request, 'RMS/user/dashboard-applied-jobs.html')

@login_required
def user_bookmark(request):
    return render(request, 'RMS/user/dashboard-saved-jobs.html')

@login_required
def user_change_password(request):
    return render(request, 'RMS/user/dashboard-change-password.html')

@login_required
def user_profile(request):
    try: 
        candidate = Candidate.objects.get(user = request.user)
        education = Education.objects.filter(candidate = request.user)
        experience = Experience.objects.filter(candidate = request.user)
    except:
        candidate = None 
        education = None
        experience = None
    
    
    context = {
        'candidate' : candidate,
        'social_medias' : social_medias,
        'education' : education,
        'experience': experience
        
    }
    return render(request, 'RMS/user/dashboard-my-profile.html', context)
