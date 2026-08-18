from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(
        max_length=50, 
        unique=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    ) 
    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.category_name 

    class Meta: 
       verbose_name_plural = "categories"

class Blog(models.Model):

    class Statuses(models.TextChoices):
        DRAFT = "draft", "Draft"
        POSTED = "posted", "Posted"

    title = models.CharField(
        max_length=50,
    )

    slug = models.SlugField( 
        max_length=100,
    )

    category = models.ForeignKey(
        Category, 
        on_delete=models.CASCADE, 
        related_name="blogs", 
    )

    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name = "blogs"
    )

    featured_image = models.ImageField(
        upload_to= "uploads/%Y/%m/%d",
    )

    short_description = models.TextField(
        max_length=500
    )

    blog_body = models.TextField(max_length=2000)

    status = models.CharField(
        max_length=20, 
        choices = Statuses, 
        default= Statuses.DRAFT

    )

    is_featured = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title