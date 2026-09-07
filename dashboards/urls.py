from django.urls import path   
from .import views


urlpatterns = [
    path('', views.dashboard , name = "dashboard"), 
    #category CRUD
    path('categories/', views.categories, name = "categories"), 
    path('categories/add/', views.add_category, name = "add_category"),
    (path('categories/edit/<int:pk>/', views.edit_category, name = "edit_category")), 
    (path('categories/delete/<int:pk>/', views.delete_category, name = "delete_category")), 
    #posts CRUD
    path('posts/', views.posts, name = "posts"), 
    path('posts/add', views.add_post, name = "add_post"), 

]