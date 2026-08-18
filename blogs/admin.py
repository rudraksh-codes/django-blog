from django.contrib import admin
from .models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        "slug" : ("title",)
    } 

    list_display = ('title', 'category', 'status', 'author', 'is_featured')
    search_fields = ('id', 'title', 'category__category_name', 'status', 'author__username')
    list_editable = ('is_featured', 'category', 'status')


# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)


