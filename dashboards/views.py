from django.shortcuts import render
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def dashboard(request):
    category_count = Category.objects.all().count()
    post_count = Blog.objects.all().count()

    context = dict(category_count = category_count, post_count = post_count)

    return render(request, "dashboard/dashboard.html", context) 

def categories(request):
    return render(request, "dashboard/categories.html")

def add_category(request):
    return render(request, "dashboard/add_category.html")