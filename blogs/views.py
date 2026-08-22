from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Category

# Create your views here.

def posts_by_category(request, category_id):
    #fetch the posts that belongs to the id = category_id 
    posts = Blog.objects.filter(category=category_id, status='posted')
    # #use try except when needed custom action on not found 
    # try:
    #     category = Category.objects.get(id = category_id)
    # except :
    #     #redirect to homepage
    #     return redirect('home')


    # use get_object_or_404 when you want to show 404 error page...
    category = get_object_or_404(Category, id = category_id) 


    context = {
        "posts" : posts , 
        'category' : category
    }

    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    pass

    blog = Blog.objects.get(slug=slug)

    context = {
        'blog' : blog   
    }

    return render(request, "blogs.html", context)