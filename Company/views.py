from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    context = {
        'latest_blog' : Blog.objects.first(),
        'blogs' : Blog.objects.all()[1:]
    }
    return render(request, 'Company/blog.html', context)

def single_blog(request, slug):
    blog = Blog.objects.get(slug = slug)
    context = {
        'blog' : blog
    }
    return render(request, 'Company/blog-details.html', context)

def contact(request):
    return render(request, 'Company/contact.html')

def about(request):
    return render(request, 'Company/about.html')

def privacy_and_policy(request):
    return render(request, 'Company/privacy-policy.html')

def faqs(request):
    return render(request, 'Company/faqs.html')