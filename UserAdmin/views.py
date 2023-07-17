from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Recruitment_System.models import Candidate, Education, Job_Posting
from django.core.paginator import Paginator
from Recruitment_System.forms import JobPostingForm
from django.contrib import messages
# Create your views here.
@login_required
def admin_index(request):
    return render(request, 'admin-user/Dashboard.html')

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
def candidate_detail_view(request, id):
    candidate = Candidate.objects.get(id=id)
    education = Education.objects.filter(candidate__id = candidate.user.id)
    context = {
        'candidate' : candidate,
        'education' : education
    }
    return render(request, 'admin-user/candidate-Detail.html', context)


@login_required
def job_board_view(request):
    form = JobPostingForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            form.save_m2m()
            messages.success(request, "Successfully Published.")
            return redirect('job-list')
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
def job_detail_view(request, pk):
    job = Job_Posting.objects.get(pk=pk)
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
def job_delete_view(request, pk):
    job = Job_Posting.objects.get(pk=pk)

    if job.delete():
        messages.success(request, 'Successfully Deleted')
        return redirect('job-list-admin')
    else:
        messages.error(request, 'Your request has not been Successfully please try again!')
        
    
    return redirect('job-detail', pk)
    

    





@login_required
def discount(request):
    return render(request, 'admin-user/discount.html')

@login_required
def Orders_detail(request):
    return render(request, 'admin-user/Orders-Detail.html')

@login_required
def order_list(request):
    return render(request, 'admin-user/Orders-List.html')

@login_required
def general_setting(request):
    return render(request, 'admin-user/Settings-General.html')


@login_required
def settings(request):
    return render(request, 'admin-user/Settings.html')

@login_required
def Shipping(request):
    return render(request, 'admin-user/Shipping.html')

@login_required
def Storefront_cart(request):
    return render(request, 'admin-user/Storefront-Cart.html')

@login_required
def Storefront_Categories(request):
    return render(request, 'admin-user/Storefront-Categories.html')

@login_required
def Storefront_Checkout(request):
    return render(request, 'admin-user/Storefront-Checkout.html')

@login_required
def Storefront_Detail(request):
    return render(request, 'admin-user/Storefront-Detail.html')

@login_required
def Storefront_Filters(request):
    return render(request, 'admin-user/Storefront-Filters.html')

@login_required
def Storefront_Home(request):
    return render(request, 'admin-user/Storefront-Home.html')

