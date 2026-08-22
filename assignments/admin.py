from django.contrib import admin

from .models import About, SocialLink

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False


# Register your models here.
admin.site.register(About, AboutAdmin)
admin.site.register(SocialLink)