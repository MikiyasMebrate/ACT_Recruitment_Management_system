from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from Company.models import Social_Media, Contact
from .forms import CandidateForm, EducationForm, ExperienceForm
from .models import Skill, Candidate, Education, Experience, Job_Posting, Bookmarks, Application
from django.contrib import messages
import csv
from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from Account.forms import CustomUserCreationForm, Login_Form
from django.core.paginator import Paginator
# Create your views here.


def csv_file_reader():
    with open('skill_data.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
            for j in i:
                    Skill.objects.create(title = j)

social_medias = Social_Media.objects.all()
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
    try: bookmark = Bookmarks.objects.filter(user=request.user).values_list('job__id', flat=True)
    except: bookmark = None
    try: candidate = Candidate.objects.get(user = request.user)
    except: candidate = None
    try: application = Application.objects.filter(user=request.user).values_list('job__id', flat=True)
    except: application = None


    job = Job_Posting.objects.filter(job_status = True)
    paginator = Paginator(job,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'social_medias' : social_medias,
        'job_list' : page,
        'bookmark' : bookmark,
        'candidate' : candidate,
        'application' : application
    }
    return render(request, 'RMS/job-list.html', context)

def job_detail(request, pk):
    job = Job_Posting.objects.get(pk=pk)
    company_info = Contact.objects.all().first()
    social_media = Social_Media.objects.all().first()
    
    print(list(job.skills.all()))
    try: bookmark = Bookmarks.objects.get(user = request.user, job = job)
    except: bookmark = None
    try: application = Application.objects.filter(user=request.user).values_list('job__id', flat=True)
    except: application = None
    context = {
        'social_medias' : social_medias,
        'job' : job,
        'company_info' : company_info,
        'social_media' : social_media,
        'bookmark' : bookmark,
        'application'  :application,
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
            return redirect('user-resume')
        else :
            messages.error(request, 'You request han not been successful please try again! ')
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
    bookmarks = Bookmarks.objects.filter(user = request.user)
    context = {
        'bookmarks' : bookmarks
    }
    return render(request, 'RMS/user/dashboard-saved-jobs.html', context)

@login_required
def user_add_bookmark(request, pk):
    try:
        check_job = Bookmarks.objects.get(job_id = pk, user = request.user)
    except: 
        check_job = False
    job = Job_Posting.objects.get(pk = pk)

    if check_job:
        messages.error(request, 'You are already Bookmarked')
        return redirect(request.META.get('HTTP_REFERER'))    
    else:
        user = request.user
        obj = Bookmarks()
        obj.user = user
        obj.job = job
        obj.save()
        messages.success(request, 'Successfully Bookmarked')
        return redirect(request.META.get('HTTP_REFERER')) 

@login_required
def user_delete_bookmark(request, pk):
    job = Bookmarks.objects.get(job__id=pk, user=request.user)

    if job.delete():
        messages.success(request, 'Successfully Removed')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Your request has not been Successfully please try again!')
        return redirect(request.META.get('HTTP_REFERER'))

@login_required
def user_apply_job(request, pk):
    try:
        applied = Application.objects.get(user = request.user, job__id = pk)
    except:
        applied = None

    education = Education.objects.filter(candidate = request.user).count()
    candidate = Candidate.objects.get(user = request.user)
    if applied is not None:
        messages.error(request, 'You are already Applied on this JOB please Check your Applied Jobs Lists')
        return redirect(request.META.get('HTTP_REFERER'))
    elif candidate is None:
        messages.error(request, 'Please Add Personal Information! ')
        return redirect('user-resume')
    elif education < 1:
        messages.error(request, 'Please at least add One Education Background!')
        return redirect('user-add-education')
    else:
        job = Job_Posting.objects.get(id=pk)
        obj = Application()
        obj.user = request.user
        obj.job = job
        obj.save()
        messages.success(request, 'Successfully Applied Check your Applied Jobs')
        return redirect(request.META.get('HTTP_REFERER'))
    
def user_cancel_job(request, pk):
    application = Application.objects.get(user = request.user, job__id=pk)
    if application.delete():
        messages.success(request, 'Successfully Canceled')
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        messages.error(request, 'Your request has not been Successfully please try again!')
        return redirect(request.META.get('HTTP_REFERER'))

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
