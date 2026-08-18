from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True, status = 'posted').order_by("updated_at")
    posts = Blog.objects.filter(is_featured=False, status = 'posted').order_by("updated_at")
    context = {
        'categories' : categories, #variable injected
        'featured_posts' : featured_posts, 
        'posts' : posts
    }
    return render(request, "home.html", context)