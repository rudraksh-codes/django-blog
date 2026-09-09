from django.shortcuts import render, redirect, get_object_or_404
from blogs.models import Category, Blog
from django.contrib.auth.decorators import login_required
from .forms import CategoryForm, PostForm   
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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


def add_post(request):

    #add logic here 
    if request.method == "POST" : 
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False) #form object -> Blog.model.instance
            post.author = request.user
            post.save()
            # title = form.cleaned_data['title']
            title = post.title
            post.slug = slugify(title) + '-' + str(post.id) #None if post.!save()
            post.save() 
            return redirect("posts")
        else:
            print(form.errors)
    else:
        form = PostForm()

    context = {
        "form" : form
    }
    
    return render (request, "dashboard/add_post.html", context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST" : 
        form = PostForm(request.POST, request.FILES,  instance=post)
        if form.is_valid():
            temp_post = form.save(commit=False)
            temp_post.slug = slugify(temp_post.title) + '-' + str(post.pk) 
            temp_post.save()
            return redirect('posts')
    form = PostForm(instance=post)
    context = {
        "form" : form, 
        "post" : post
    }
    return render(request, "dashboard/edit_post.html", context)

def delete_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    if request.method == "POST" : 
        post.delete()
        return redirect('posts')
    

    return render(request, "dashboard/delete_post.html")

def users(request):
    users = User.objects.all()
    context = dict(users=users)
    return render(request, "dashboard/users.html", context)