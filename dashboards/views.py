from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm

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
    if request.method == "POST" : 
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
        else : 
            print(form.errors)
    else : 
        form = CategoryForm()
    context = {
        "form" : form
    }
    return render(request, "dashboard/add_category.html", context)


def edit_category(request, pk):
    category = get_object_or_404(Category, pk = pk)
    if request.method == "POST" : 
        form  = CategoryForm(request.POST, instance=category) #new_value, #existing_value
        if form.is_valid():
            form.save()
            return redirect("categories")
    form = CategoryForm(instance=category)
    context = {
        "form" : form,
        "category" : category, 
    }
    return render(request, "dashboard/edit_category.html", context)


def delete_category(request, pk):
    category = get_object_or_404(Category, pk = pk)
    if request.method == "POST" :
        category.delete()
        return redirect("categories")
    return render(request, "dashboard/delete_category.html")


def posts(request):
    posts = Blog.objects.all()
    context = dict(posts = posts)
    return render(request, "dashboard/posts.html", context)  