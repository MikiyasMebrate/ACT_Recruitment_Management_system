from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'Company/blog.html')

def single_blog(request):
    return render(request, 'Company/blog-details.html')

def contact(request):
    return render(request, 'Company/contact.html')

def about(request):
    return render(request, 'Company/about.html')

def privacy_and_policy(request):
    return render(request, 'Company/privacy-policy.html')

def faqs(request):
    return render(request, 'Company/faqs.html')