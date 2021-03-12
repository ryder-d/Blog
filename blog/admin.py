from django.contrib import admin
from .models import Post

# Defines the display and order of fields in Django admin
class PostAdminPanel(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    # TODO auto slug https://www.codegrepper.com/code-examples/python/django+admin+slug+auto+populate
    prepopulated_fields = {'slug': ('title',)}

# # Register the model for posts so they show in /admin  
admin.site.register(Post, PostAdminPanel)

