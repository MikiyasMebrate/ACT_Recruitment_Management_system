from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Recruitment_System.models import Candidate, Education,Interviews, Job_Posting, Sector, Application, Experience
from django.core.paginator import Paginator
from Recruitment_System.forms import JobPostingForm, SectorForm,ApplicationForm, InterviewForm
from django.contrib import messages

# Create your views here.
@login_required
def admin_index(request):
    return render(request, 'admin-user/Dashboard.html')


#Candidate
@login_required
def candidate_view(request):
    candidate_list = Candidate.objects.all()
    paginator = Paginator(candidate_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    
    context = {
        'candidates' : page
    }
    return render(request, 'admin-user/candidate-List.html', context)

@login_required
def candidate_detail_view(request, slug):
    candidate = Candidate.objects.get(slug=slug)
    education = Education.objects.filter(candidate__id = candidate.user.id)
    experience = Experience.objects.filter(candidate__id = candidate.user.id)
    application = Application.objects.filter(user__id = candidate.user.id)
    context = {
        'candidate' : candidate,
        'educations' : education,
        'experiences' : experience,
        'applications' : application
    }
    return render(request, 'admin-user/candidate-Detail.html', context)


#JOB
@login_required
def job_board_view(request):
    form = JobPostingForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            messages.success(request, "Successfully Published.")
            return redirect('job-list-admin')
        else:
            messages.error(request, "Your request has not been Unsuccessful Please try again!")
    
    job_list = Job_Posting.objects.all()
    paginator = Paginator(job_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    context = {
        'job_list' : page,
        'form' : form
    }
    return render(request, 'admin-user/job-List.html', context)

@login_required
def job_detail_view(request, slug):
    job = Job_Posting.objects.get(slug=slug)
    form = JobPostingForm(request.POST or None, instance=job)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Published.")
            return redirect('job-list-admin')
        else:
            messages.error(request, "Your request has not been Unsuccessful Please try again!")
        
    context = {
        'form' : form,
        'job' : job
    }
    return render(request, 'admin-user/job-Detail.html', context)

@login_required
def job_delete_view(request, slug):
    job = Job_Posting.objects.get(slug=slug)

    if job.delete():
        messages.success(request, 'Successfully Deleted')
        return redirect('job-list-admin')
    else:
        messages.error(request, 'Your request has not been Successfully please try again!')
        
    
    return redirect(request.META.get('HTTP_REFERER'))



#Sector
@login_required
def department(request):
    department = Sector.objects.all()
    form = SectorForm(request.POST or None)
    paginator = Paginator(department,10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        if form.is_valid():
           form.save()
           messages.success(request, 'Successfully Published.')
           return redirect('department-admin')
        else:
            messages.error(request, 'Your request has not been Unsuccessful Please try again!')
    context = {
        'departments' : page,
        'form' : form
    }
    return render(request, 'admin-user/department-list.html', context)

@login_required
def department_detail(request, slug):
    department = Sector.objects.get(slug = slug)
    form = SectorForm(request.POST or None, instance=department)
    job_list = Job_Posting.objects.filter(sector__slug = slug)
    paginator = Paginator(job_list,5)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Published.")
            return redirect('department-admin')
        else:
            messages.error(request, "Your request has not been Unsuccessful Please try again!")
    context = {
        'form' : form,
        'department' : department,
        'job_list' : page
    }

    return render(request, 'admin-user/department-detail.html', context)

@login_required
def department_delete(request, slug):
    job = Sector.objects.get(slug=slug)

    if job.delete():
        messages.success(request, 'Successfully Deleted')
        return redirect('department-admin')
    else:
        messages.error(request, 'Your request has not been Successfully please try again!')
        
    return redirect(request.META.get('HTTP_REFERER'))
  

#Applicant
@login_required
def applicant_all(request):
    job_post = Job_Posting.objects.filter(job_status =True)
    sector = Sector.objects.filter()
    applicants = Application.objects.filter(job__job_status =True)

    paginator = Paginator(applicants,15)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'sectors' : sector,
        'job_list' : job_post,
        'applicants' : page,
    }
    return render(request, 'admin-user/applicant-sector.html', context)

def applicant_category(request, slug):
    job_post = Job_Posting.objects.filter(job_status =True)
    selected_job = Job_Posting.objects.get(slug = slug)
    sector = Sector.objects.filter()
    applicants = Application.objects.filter(job__job_status =True, job = selected_job)

    paginator = Paginator(applicants,15)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'sectors' : sector,
        'job_list' : job_post,
        'applicants' : page,
    }
    return render(request, 'admin-user/applicant-sector.html', context)

def applicant_detail(request, slug, slug2):
    candidate = Candidate.objects.get(slug=slug)
    education = Education.objects.filter(candidate__id = candidate.user.id)
    experience = Experience.objects.filter(candidate__id = candidate.user.id)
    application_applicant = Application.objects.get(user__id = candidate.user.id, job__slug = slug2)
    
    try : interview = Interviews.objects.get(application = application_applicant)
    except: interview = None
    form = ApplicationForm(request.POST or None, instance=application_applicant)
    interview_form = InterviewForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            if form.save():
                messages.success(request, f'Successfully Changed .')
        
        if interview_form.is_valid():
            obj = interview_form.save(commit=False)
            obj.application = application_applicant
            obj.save()
            messages.success(request, 'Successfully Transferred into Interview .')
        
        return redirect(request.META.get('HTTP_REFERER'))

    context = {
        'candidate' : candidate,
        'educations' : education,
        'experiences' : experience,
        'application_applicant' : application_applicant,
        'form' : form,
        'interview_form' : interview_form,
        'interview': interview
    }
    return render(request, 'admin-user/candidate-Detail.html', context)