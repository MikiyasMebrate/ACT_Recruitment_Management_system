from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Blog, Comment
from .forms import CommentForm
# Create your views here.
def blog(request):
    latest_blog = Blog.objects.first()
    blogs = Blog.objects.all().exclude(id = latest_blog.id)
    

    paginator = Paginator(blogs, 9)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'latest_blog' : latest_blog,
        'blogs' : page
    }
    return render(request, 'Company/blog.html', context)

def single_blog(request, slug):
    blog = Blog.objects.filter(slug = slug).first()
    latest_post = Blog.objects.all().exclude(slug = slug)[:4]
    comments =  Comment.objects.filter(blog__pk = blog.pk)
   
    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.save()
            form = CommentForm()
    else:
         form = CommentForm()
            

    context = {
        'blog' : blog,
        'latest_posts' : latest_post,
        'form' : form,
        'comments' : comments
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