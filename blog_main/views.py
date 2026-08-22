from django.shortcuts import render
from blogs.models import Blog
from assignments.models import About, SocialLink

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status = 'posted').order_by("updated_at")
    posts = Blog.objects.filter(is_featured=False, status = 'posted').order_by("updated_at")

    #fetch about us 
    try:
        about = About.objects.get()
    except:
        about = None


    context = {
        'featured_posts' : featured_posts, 
        'posts' : posts, 
        'about' : about, 
    }
    
    return render(request, "home.html", context)