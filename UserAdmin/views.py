from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Recruitment_System.models import Candidate, Education,Interviews, Job_Posting, Sector, Application, Experience
from django.core.paginator import Paginator
from Recruitment_System.forms import JobPostingForm, SectorForm,ApplicationForm, InterviewForm
from django.contrib import messages
from Account.models import CustomUser
from Account.forms import CustomUserCreationForm
from Account.decorators import admin_user_required
from django.db.models import Q
from django.contrib.sessions.models import Session
from django.utils import timezone
from Company.models import Comment
from Company.models import Blog, Blog_Categories
from .forms import BlogForm
import os
import telebot
from bs4 import BeautifulSoup

# Create your views here.



BOT_TOKEN = os.environ.get('6195701188:AAGYJvuebbXWUatD4MtOwJ8NNASCdMlXjwE')
bot = telebot.TeleBot('6195701188:AAGYJvuebbXWUatD4MtOwJ8NNASCdMlXjwE')
channel_name = '@act_job_board'




@login_required
@admin_user_required
def admin_index(request):
    count_user = CustomUser.objects.count()
    total_jobs = Job_Posting.objects.count()
    sector = Sector.objects.count()
    now = timezone.now()
    live_sessions = Session.objects.filter(expire_date__gte=now).count()
    hired = Interviews.objects.filter(application__status = 'hired').count()
    total_comment = Comment.objects.count 
    recent_jobs = Job_Posting.objects.all()[:10]
    sectors = Job_Posting.objects.all()[:10]

    sector_data = []
    for i in sectors:
        graph = {
            i.title : i.count_applicant()
        }
        sector_data.append(graph)
    
    sector_data_list = [[k.lower().replace(' ', '-'), v] for d in sector_data for k, v in d.items()]
    print(sector_data_list)

                     

    context = {
        'count_user' : count_user,
        'live_sessions' : live_sessions,
        'total_jobs' : total_jobs,
        'sector' : sector,
        'hired' : hired,
        'comment' : total_comment,
        'recent_jobs' : recent_jobs,
        'sector_data' : sector_data_list
    }
    return render(request, 'admin-user/Dashboard.html', context)


#Candidate
@login_required
@admin_user_required
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
@admin_user_required
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
@admin_user_required
def job_board_view(request):
    form = JobPostingForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            title = obj.title
            sector = obj.sector
            description = BeautifulSoup(obj.description, 'html.parser').text
            experience = obj.experience
            vacancies = obj.vacancies
            location = obj.location 
            salary_range_start = obj.salary_range_start
            salary_range_final  = obj.salary_range_final
            type = obj.type
            date_closed = obj.date_closed

            obj.save()
            form.save_m2m()

            skills = obj.skills.all()
            skill_names = [str(skill) for skill in skills]
            skills = ', '.join(skill_names)


            text = f'''@act_job_board
ACT American College of Technology\n
JOB BOARD\n
- Job Title: {title}\n
- Sector: {sector}\n
- Vacancies: {vacancies}\n
- Job Type: {type}\n
- Experience: {experience}\n
- Description: {description}\n
- Skills: {skills}\n
- Location: {location}\n
- Date Close: {date_closed}\n
- Salary: {salary_range_start} - {salary_range_final}\n
            
 '''
            try: bot.send_message(chat_id=channel_name, text=text)
            except: pass
                        

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
@admin_user_required
def job_detail_view(request, slug):
    job = Job_Posting.objects.get(slug=slug)
    form = JobPostingForm(request.POST or None, instance=job)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)

            title = obj.title
            sector = obj.sector
            description = BeautifulSoup(obj.description, 'html.parser').text
            experience = obj.experience
            vacancies = obj.vacancies
            location = obj.location 
            salary_range_start = obj.salary_range_start
            salary_range_final  = obj.salary_range_final
            type = obj.type
            date_closed = obj.date_closed

            obj.save()
            form.save_m2m()

            skills = obj.skills.all()
            skill_names = [str(skill) for skill in skills]
            skills = ', '.join(skill_names)


            text = f'''@act_job_board
ACT American College of Technology\n
JOB BOARD\n
- Job Title: {title}\n
- Sector: {sector}\n
- Vacancies: {vacancies}\n
- Job Type: {type}\n
- Experience: {experience}\n
- Description: {description}\n
- Skills: {skills}\n
- Location: {location}\n
- Date Close: {date_closed}\n
- Salary: {salary_range_start} - {salary_range_final}\n
            
 '''
            try: bot.send_message(chat_id=channel_name, text=text)
            except: pass


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
@admin_user_required
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
@admin_user_required
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
@admin_user_required
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
@admin_user_required
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
@admin_user_required
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

@login_required
@admin_user_required
def applicant_category(request, slug):
    job_post = Job_Posting.objects.filter(job_status =True)
    selected_job = Job_Posting.objects.get(slug = slug)
    sector = Sector.objects.filter()
    applicants = Application.objects.filter(job__job_status =True, status = 'pending',job = selected_job)


    paginator = Paginator(applicants,15)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'sectors' : sector,
        'job_list' : job_post,
        'applicants' : page,
    }
    return render(request, 'admin-user/applicant-sector.html', context)

@login_required
@admin_user_required
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
        if form.is_valid() and interview_form.is_valid():
            obj = form.save(commit=False)
            obj.status = 'in_review'
            obj.save()

            obj_interview = interview_form.save(commit=False)
            obj_interview.application = application_applicant
            obj_interview.save()

            messages.success(request, f'Successfully Changed .')
            return redirect(request.META.get('HTTP_REFERER'))
        
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


#Accounts
@login_required
@admin_user_required
def admin_account_list(request):
    accounts = CustomUser.objects.filter(Q(is_superuser = True)| Q(is_admin = True ) |Q(is_interviewer = True))
    form = CustomUserCreationForm(request.POST or None, request.FILES or None)

    paginator = Paginator(accounts,10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)


    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully created.')
    
    context = {
        'accounts' : page,
        'form':form
    }
    return render(request, 'admin-user/admin-list.html', context)


#BLOG
@login_required
@admin_user_required
def blog_lists(request):
    try:
        latest_blog = Blog.objects.first()
        blogs = Blog.objects.all().exclude(id = latest_blog.id)
    except:
        latest_blog  = None
        blogs = None

    blog_form = BlogForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('admin-blog-list')

    paginator = Paginator(blogs, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'latest_blog' : latest_blog,
        'blogs' : page,
        'blog_form' : blog_form
    }
    return render(request,'admin-user/blog.html',context )

@login_required
@admin_user_required
def blog_detail(request, slug):
    blog = Blog.objects.filter(slug = slug).first()
    latest_post = Blog.objects.all().exclude(slug = slug)[:4]
    comments =  Comment.objects.filter(blog__pk = blog.pk)
   
    blog_form = BlogForm(request.POST or None, request.FILES or None, instance=blog)
    if request.method == 'POST':
        if blog_form.is_valid():
            blog_form.save()
            messages.success(request, 'Successfully Updated')
            return redirect('admin-blog-list')
            

    context = {
        'blog' : blog,
        'latest_posts' : latest_post,
        'comments' : comments,
        'blog_form' : blog_form
    }
    return render(request,'admin-user/blog-detail.html', context)